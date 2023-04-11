# Use an official Python runtime as a parent image
FROM python:3.10.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the Django app code into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django app server
CMD ["gunicorn", "api.wsgi"]