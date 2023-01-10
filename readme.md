# Jupyter Notebook visulization Technique

## Prerequisites:
- Functional Docker instalation, with enouhg disk space to freely download images and containers
- Modern webbrowser (Firefox recomeneded)

# Option 1: Building Image and Container Form Source:
This option involves obtaining the data and source code from the git repository and building the docker image and container yourself
## Building The Container
This method of deployment works throgh encapsualating the nessecary data and vizulisatoin technique inside of a docker container such that any user who is able to maintian the container runtime is able to run and visulize the data. 

### Step 1. Obtaining the source
Clone this branch of the repository using the followign command:

```git clone https://github.com/Biomedical-Simulation-Lab/web-viz.git -b jupyterNotebook ```
### Step 2. Building the Image
Navigate into the source directory and vierify that the Dockerfile is present and run the following command.

```docker build . --tag jupyter_notebook_viz```

### Step 3. Testing The Image

Run the following command to build a test container using the image that was created in the previous step to verify that their are no problems with the deployment

``` docker run --name test_jupyter_notebook -p 8888:8888 jupyter_notebook_viz```

If the command ran sucesfully you should see two ip adresses appear, click the 2nd ont and open it in a modern browser (Firefox is recomeneded) and should see the following output.

![Alt Text](/figures/jupyter_notebook_landing_page.png)

