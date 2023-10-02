# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to work directory
COPY requirements.txt .

# Install packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available outside container
EXPOSE 5000

# Run the Flask Application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
