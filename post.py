from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    
@app.post("/items/")  #post method of API
# to check this POST request you need to put the 
# specified url in the POSTMAN and it will give you
# responding status code(200 means ok)
# in the Body parameter under raw give this 
#  {
#   "name": "arbaz",
#    "description": "software engineer"
#}
def create_item(item: Item):
    return item