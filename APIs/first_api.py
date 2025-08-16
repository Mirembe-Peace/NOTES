from fastapi import FastAPI

app = FastAPI()
@app.get("/myFirstAPI")

def myFirstAPI(name: str, age: int):
    if name == "Peace" and age ==  21:
        return{"Mercy this is your first API": 1}
    else:
        return{"you are not Mercy 🙄": 0}
