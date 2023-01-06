FROM ghcr.io/pyvista/pyvista:latest

COPY LNH_Visualization.ipynb /home/jovyan/
COPY data/* /home/jovyan/data/