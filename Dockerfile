# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the entrypoint command to run the Flask app
CMD ["python", "rest_app.py"]
