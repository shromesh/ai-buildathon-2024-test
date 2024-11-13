# Use the official Python image
FROM python:3.12

# Update and upgrade system packages
RUN apt-get -y update && apt-get -y upgrade

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the FastAPI application code
COPY app/ /usr/src/app/

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the FastAPI application with reload enabled
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
