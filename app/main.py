from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Python CI/CD with Docker and ArgoCD"}

@app.get("/health")
def health():
    return {"status": "healthy"}