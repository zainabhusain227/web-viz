# Flask Webapp Visulization Technique

## Prerequisites:

- Python3 or greater
- Docker instalation
- Modern web browser
- Deployment platform (Details provided for heroku)

## Building The Container:
This app was build to be deployed onto a heroku free tier dyno, but any service that supports containerized deployments of web applications should support it, but some modifications may be required.

### Step 1. Obtaining The Source
Clone this branch of the source repository using the following command:

``` git clone https://github.com/Biomedical-Simulation-Lab/web-viz.git -b flaskWebApp```

### Step 2. Building the Container
Navitate into the source directory and vertify that the Dockerfile is present and run the following command.

```docker build . --tag flask_viz_app```

This will buiild a docker image that contains all of the nessecary dependancies and data for the app to allow you to visulize it

### Step 3. Testing the Container Image

Run the following command that will build a container from the image that was previously built.

``` docker run --name test_flask_app flask_viz_app ```

If this command runs sucesfully your terminal should see two ip adresses appear, click the 2nd one to open it in a modern browser (Firefox recomended) and see the following output.

![Alt Text](/figures/sucesfull_test.png)

## Deploying the Container:
This section assumes you will be deploying the container to the heroku web hosting service, however most web hosting applications will support a contaierized release (AWS ECS service is another popular option, but is slightly less user friendly)

### Login to Heroku

Inorder to deploy your cotainer to the web using the command line using heroku you must install and log into the heroku-cli tool using the followig guide (https://devcenter.heroku.com/articles/heroku-cli)

Following your sucesfull instalation and login to the service execute the following two commands substuting your relevant paramaters into the commands

```heroku container:push web --app YOUR_APP_NAME```

This command will push your container to your application on heroku to prime it for release

```heroku container:release web --app bsl-web-viz```

This command will release your container to the web such that is may be accessed by anyone with the link to your deployment

# WARNING:
This will deploy you application to the production enviroment, please configure your indidual deployment as you see fit and do not use this guide for any more then a reference