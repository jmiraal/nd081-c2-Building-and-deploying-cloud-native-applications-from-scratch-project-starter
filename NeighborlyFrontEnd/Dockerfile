# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7-appservice
# Base the image on the built-in Azure Functions Python image
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7
ENV host:logger:consoleLoggingMode=always

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

EXPOSE 80

# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt

## Copy app to image
## to run the image: docker run -p 8080:5000 -it neighborlywebimage
## to test the app in local: localhost:8080

WORKDIR /NeighborlyFrontEnd
COPY . .

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]