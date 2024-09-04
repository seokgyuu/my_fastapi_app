from fastapi import APIRouter
from fastapi import  Path #  path Variable 객체

# 라우터 생성
router = APIRouter(tags=['todos'])


# TODO 목록 불러오기
@router.get("/todos")
async def get_todos():
    return ["소"]

# 새 TODO 생성
@router.post("/todos")
async def add_todo():
    pass

# TODO 변경
@router.put("/todos/{todo_id}")
async def modify_todo(todo_id: int = Path(
    ..., #필수 필드
    title="Todo Id",
    description="수정할 Todo 아이템의 ID",
    ge=1, #1이상
    le=100 # 100이하
)):
    pass

# TODO 삭제
@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int =Path(
    ...,
    title="Todo ID",
    description="삭제할 Todo 아이템의 ID"
)):
    pass