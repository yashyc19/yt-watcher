# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y sudo openvpn python3-pip && \
    pip install protonvpn-cli

# Ensure protonvpn-cli is in the PATH
ENV PATH="/root/.local/bin:${PATH}"

# Initialize ProtonVPN CLI
RUN echo "yashyc19@gmail.com\nmessi2001" | /root/.local/bin/protonvpn-cli login

# Make the test.py file executable
RUN chmod +x test.py

# Run test.py when the container launches
CMD ["python", "test.py"]