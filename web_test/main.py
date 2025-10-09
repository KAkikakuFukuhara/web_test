from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from .routers import brouse, api


app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="web_test/static"), name="static")


@app.get("/api/hello")
async def hello():
    return {"message": "hello worlds!"}


app.include_router(api.router)
app.include_router(brouse.router)

