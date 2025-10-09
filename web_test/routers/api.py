from typing import Optional
import pprint

from fastapi import APIRouter, Request, Form, Body
from ..schemas.post_test import PostTest

router = APIRouter()

@router.post("/api/post-test")
async def post_test(
        post_test: PostTest):
    print(post_test)
    pass

