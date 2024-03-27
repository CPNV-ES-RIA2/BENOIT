# Base Stage for shared environment setup
FROM python:3.8-slim as base

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file, to cache the dependencies installation
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Flask application file
COPY APIGatewayServer.py .

# Development stage builds on top of the base stage
FROM base as development
# Set environment variable to indicate development environment
ENV FLASK_ENV=development
ENV FLASK_APP=APIGatewayServer.py
# Expose port 5170 for the Flask development server
EXPOSE 5170
# Run the Flask development server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5170"]

# Production stage also builds on the base stage
FROM base as production
# Set environment variable to indicate production environment
ENV FLASK_ENV=production
ENV FLASK_APP=APIGatewayServer.py
# Expose port 5170 for access to the Flask application
EXPOSE 5170
# Running Flask directly for simplicity as per request
CMD ["flask", "run", "--host=0.0.0.0", "--port=5170", "--without-threads"]
