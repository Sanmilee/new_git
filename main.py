#pip install fastapi
#pip install uvicorn

# uvicorn main1:app --reload
# http://127.0.0.1:8000



### Display "Hello: Welcome Lee"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello: Welcome Lee"


