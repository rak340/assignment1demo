# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your Python script into the container
COPY app.py .

# Set the command to run the app
CMD ["python", "app.py"]
