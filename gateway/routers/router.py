from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {
        f"{__name__}": "root page"
    }
