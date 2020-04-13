#Use python as base image
FROM python:3.7.7-slim

#Use working directory /app
WORKDIR /app

#copy all the contents of current directory
ADD . /app

#installing required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#open port 5000
EXPOSE 5000

#set enviornment variable
ENV NAME OpentoAll

#run python program
CMD ["python","app.py"]
