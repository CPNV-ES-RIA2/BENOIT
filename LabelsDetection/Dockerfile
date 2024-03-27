# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies including libmagic
RUN apt-get update && apt-get install -y \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your application
COPY . .

# Make port 5171 available to the world outside this container
EXPOSE 5171

# Define environment variable
ENV FLASK_APP=LabelServer.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5171"]
