
#Use an offical python runtime as the base image

FROM python:3.12.4

#Set the working directory in the container
WORKDIR /app

#Copy Python script to the container
COPY hello.py .

#Run the Python Script when the container launches
CMD [ "python", "hello.py" ]