# Use a base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your Python script into the container
COPY app.py .

# Install required libraries
RUN pip install --no-cache-dir scikit-learn numpy

# Run the app
CMD ["python", "app.py"]
