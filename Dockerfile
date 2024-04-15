# Use the official lightweight Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app.py

# Install dependencies
COPY requirements.txt /app.py/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app.py/

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"] 
