from fastapi import FastAPI

app = FastAPI()     

@app.get("/")
def root_url():
    return {"message": "welcome to FastApi"}

