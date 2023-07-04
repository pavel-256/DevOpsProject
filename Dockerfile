# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python scripts to the working directory
COPY db_connector.py .
COPY rest_app.py .

# Expose the port that the Flask server will listen on
EXPOSE 5000

# Run the rest_app.py script
CMD ["python", "rest_app.py"]
