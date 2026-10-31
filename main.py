from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import socket

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/hello")
def hello():
    return FileResponse("hello.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/pod")
def pod():
    return {"pod": socket.gethostname()}

if __name__ == "__main__":
    uvicorn.run("main:app",host ="127.0.0.1", port=8000, reload = True)


