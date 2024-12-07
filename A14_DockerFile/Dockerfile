# Start with a base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files to the working directory in the container
COPY . /app

# Install dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the application
CMD ["python", "app.py"]

