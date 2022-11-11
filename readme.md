This is a repoisity that deploys a pyvista flask application to a heroku web app.

Run the following commands to deploy:

docker build .

# Building docker image 
docker build --tag IMAGENAME .

# Running docker image to test your changes

docker run IMAGENAME


# To push the app to heroku run

heroku container:push web --app bsl-web-viz

heroku container:release web --app bsl-web-viz