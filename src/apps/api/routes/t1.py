from fastapi import APIRouter

from fast_tmp.models import Group, User

router = APIRouter(prefix="/t1")


@router.get("/user")
async def user_list():
    return await User.all()


@router.get("/group")
async def group_list():
    return await Group.all()
