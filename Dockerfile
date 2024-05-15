# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local libraries and configuration files into the container
COPY libs /app/libs
COPY config /app/config
COPY requirements.txt /app
COPY model /app/model
# Copy the current directory contents into the container at /app
# Install OpenGL libraries
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get update && apt-get install -y libglib2.0-0

COPY streamlit_main.py /app
RUN apt-get update && apt-get install -y gcc python3-dev

# Install any needed dependencies specified in requirements.txt
RUN pip install  -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Run the Streamlit application when the container launches
CMD ["streamlit", "run", "streamlit_main.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]
