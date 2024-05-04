from fastapi import FastAPI # type: ignore


app = FastAPI() #created an instance of FAST-API Class  
    
@app.get("/") #get -method API
def response():
    return {"Hi from fast api"}

@app.get("/help") #route
def new_response():
    return {'Hi how can we help you?'}
