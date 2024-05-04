# FastApi
To create a simple fast api in python we need to do these :
1. Inside your env , install fastapi
2. Import the necessary modules from FastAPI library
3. Create an instance of the FastAPI class
4. To run this fast api file you need to install uvicorn inside your env.
5. Then use uvicorn to run the main function which is our app(FastAPI) instance.
6. uvicorn <your file name without the extension>:app --reload this is the command to run the .py file.
7. Use port 8000 as default for running the server . You can change it if needed.
#how to set up env steps 
1. python3 -m venv .env
2. source .env/bin/activate
whenever the post request is made you still cannot see your data
on the web url(8000) port becuase that works on a GET request.
to fix this issue:
we will check it inside POSTMAN:
1. select the type of request
2. paste the url with the endpoint
3. And in the Body parameter under Raw add this
{
    "name": "arbaz",
    "description": "software engineer"
}
4. now after running it on your vscode you can send that request in postman.