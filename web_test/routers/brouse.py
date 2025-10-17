from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


TAG_BROUSE = "brouse"

router = APIRouter()
templates = Jinja2Templates("web_test/templates")


@router.get(
    "/hello",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_hello(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("hello.html", context)


@router.get(
    "/",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@router.get(
    "/operate",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_operate(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("operate.html", context)


@router.get(
    "/detail",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_detail(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("detail.html", context)


@router.get(
    "/camera",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_camera(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("camera.html", context)


@router.get(
    "/notification",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_notification(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("notification.html", context)


@router.get(
    "/post-test",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_post(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("post-test.html", context)


@router.get(
    "/management",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_management(request: Request):
    return templates.TemplateResponse(request, "management.html")


@router.get(
    "/management/add_robot",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_add_robot(request: Request):
    return templates.TemplateResponse(request, "managements/add_robot.html")


@router.get(
    "/management/update_robot",
    response_class=HTMLResponse,
    tags=[TAG_BROUSE])
async def read_update_robot(request: Request):
    return templates.TemplateResponse(request, "managements/update_robot.html")


