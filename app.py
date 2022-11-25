"""Simple flask app to display dynamic threejs generated from pyvista.

Expected paths:
dynamic_ex/
└── app.py
    templates/
    └── index.html

"""
import os

from flask import Flask, render_template, request
import numpy as np

import pyvista
from pyvista import examples


static_image_path = os.path.join('static', 'images')
if not os.path.isdir(static_image_path):
    os.makedirs(static_image_path)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/getimage")
def get_img():
    """Generate a screenshot of a simple pyvista mesh.

    Returns
    -------
    str
        Local path within the static directory of the image.

    """
    # get the user selected mesh option
    meshtype = request.args.get('meshtype')
    color = request.args.get('color')
    style = request.args.get('style')
    print(f"'{style}'")
    op_percent=request.args.get('StreamlineTransparency')
    op= int(op_percent)/100

    # bool types
    show_edges = request.args.get('show_edges') == 'true'
    lighting = request.args.get('lighting') == 'true'
    pbr = request.args.get('pbr') == 'true'
    anti_aliasing = request.args.get('anti_aliasing') == 'true'

    if meshtype == 'Sphere':
        mesh = pyvista.Sphere()
    elif meshtype == 'Cube':
        mesh = pyvista.Cube()
    elif meshtype == 'Bohemian Dome':
        mesh = pyvista.ParametricBohemianDome()
    elif meshtype == 'Cylinder':
        mesh = pyvista.Cylinder()
    elif meshtype == 'Vectors':
        n_points = 20
        points = np.random.random((n_points, 3))
        poly = pyvista.PolyData(points)
        poly['direction'] = np.random.random((n_points, 3))
        poly['direction'] -= poly['direction'].mean(axis=0)  # normalize
        mesh = poly.glyph(geom=pyvista.Arrow(), orient=True, scale=True, factor=0.2)
        # reset color as we will want to see the colors of the arrows
        color = None

    elif meshtype == 'LNH':
        #print(request.args.get('show_edges'))
        ####this is the slider parameter to adjust lnh thresholding (values 0 to 1)#####
        #lnh_thresh_percent= request.form["LNHThreshValue"]
        lnh_thresh= 0.7 #lnh_thresh_percent/100
        ####this is the slider parameter to adjust streamline opacity (values 0 to 1)#####
        #streamline_op_percent= request.args.get('rangeValue')
        #int_stream= int(streamline_op_percent)
        streamline_op= 1 #streamline_op_percent/100

        lnh_data = pyvista.read('data/lnh_final.vtk')
        lnh_data.flip_z(inplace=True)
        streamline_data= pyvista.read('data/streamline_final.vtk')
        streamline_data.flip_z(inplace=True)
        mesh=streamline_data


    elif meshtype == 'Queen Nefertiti':
        mesh = examples.download_nefertiti()
    elif meshtype == 'Lidar':
        mesh = examples.download_lidar()
    else:
        # invalid entry
        raise ValueError('Invalid Option')

    # generate screenshot
    filename = 'mesh.html'
    filepath = os.path.join(static_image_path, filename)

    # create a plotter and add the mesh to it
    p = pyvista.Plotter(window_size=(600, 600))
    # pl.add_mesh(
    #     mesh,
    #     style=style,
    #     lighting=lighting,
    #     pbr=pbr,
    #     metallic=0.8,
    #     split_sharp_edges=True,
    #     show_edges=show_edges,
    #     color=color,
    # )
    p.add_mesh(mesh, style=style, lighting=lighting, opacity=op)
    '''
    lnh_data.set_active_scalars('LNH')
    #lnh ranges from -1 to 1, we must calculate the negative lnh threshold as well (is if threshold is 0.5 we will plot values above 0.5 and below -0.5)
    neg_lnh_thresh= float (0) - float(lnh_thresh)
    #create 2 new meshes, one for the thresholded positive points 
    pos_lnh= lnh_data.threshold(lnh_thresh)
    #and 1 for the thresholded negative points
    neg_lnh= lnh_data.threshold(neg_lnh_thresh,invert=True)

    #plot the streamlines mesh
    p.add_mesh(streamline_data, name="Streamlines", color='purple',opacity=streamline_op)

    #plot the 2 meshes
    p.add_mesh(pos_lnh, name="lnh_pos", color='red', opacity=1)
    p.add_mesh(neg_lnh, name="lnh_neg", color='blue',opacity=1) '''

    if anti_aliasing:
        p.enable_anti_aliasing()
    p.background_color = 'white'
    p.export_html(filepath)
    return os.path.join('images', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)