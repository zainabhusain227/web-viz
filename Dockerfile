# Use buildx to enable use across multiple computer architectures
# FROM docker
# COPY --from=docker/buildx-bin:latest /buildx /usr/libexec/docker/cli-plugins/docker-buildx
# RUN docker buildx version

# start by pulling the python image
FROM ubuntu:latest

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install python3-pip -y
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT ["python3"]
CMD ["app.py"]