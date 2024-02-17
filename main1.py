from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def index():
    return {"data":{"name":"Jay Borade"}}


@app.get("/about")
def about_page():
    return {"data":{"About":"This is about page"}}