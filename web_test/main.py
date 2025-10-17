from argparse import ArgumentParser

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
import uvicorn

from web_test.routers import brouse, api

## グローバル変数にしないと`reload`が実行されない。
app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="web_test/static"), name="static")

app.include_router(api.router)
app.include_router(brouse.router)


def add_argument(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument("--reload", action="store_true")
    return parser


def main(*args, **kwargs):
    if kwargs['reload']:
        ## 最初だけ実行される。reload時には`main`は実行されない。
        uvicorn.run("main:app", reload=kwargs['reload'])
    else:
        ## こっちはグローバル変数じゃなくても実行できる
        uvicorn.run(app)


if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser()
    parser = add_argument(parser)
    main(**vars(parser.parse_args()))
