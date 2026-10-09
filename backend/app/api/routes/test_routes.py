from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/test", tags=["test"])


class TestResponse(BaseModel):
    message: str


@router.get("", response_model=TestResponse)
def get_test() -> TestResponse:
    return TestResponse(message="Backend connected successfully")
