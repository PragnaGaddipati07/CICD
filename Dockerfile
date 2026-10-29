# Specifies the base image
FROM python:3.12-slim
# Defines the working directory within the container
WORKDIR /app
# Copies files/directories from host to image
COPY requirements.txt .
# Execute commands during image build
RUN pip install -r requirements.txt

#Copies app files into the container
COPY main.py hello.html index.html ./

#Tells Docker that app uses port 8000
EXPOSE 8000

#This command executes when container starts
CMD ["python", "-m","uvicorn","main:app","--host","0.0.0.0","--port","8000"]
