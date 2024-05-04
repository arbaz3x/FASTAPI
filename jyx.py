from fastapi import FastAPI

app = FastAPI() #created an instance of FAST-API Class

@app.get("/") #route
def response():
    return {"Hi from fast api"}

@app.get("/help") #route
def new_response():
    return {'Hi how can we help you?'}