# Base image
FROM python:3.9

# Set the working directory in the container
# Use a base image with the desired operating system and dependencies
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install required Python modules
RUN pip install --no-cache-dir flask pymysql selenium requests

# Expose the port on which the application will listen
EXPOSE 5000

# Specify the command to run the application
CMD ["python", "rest_app.py"]
