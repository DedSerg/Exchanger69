from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/users")
async  def get_all_user():
    pass

@router.get("/user_id")
async  def get_user_by_id():
    pass

@router.post("/create")
async  def create_user():
    pass

@router.put("/update")
async  def update_user():
    pass

@router.delete("/delete")
async  def delete_user():
    pass