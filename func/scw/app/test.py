
from fastapi import APIRouter

router = APIRouter(
    tags=["test"]
)

@router.get("/writefile", description="测试写文件")
def write_file():
    with open("test.txt","w") as f:
        f.write("test")
    return {"status":"ok"}

@router.get("/readfile", description="测试读文件")
def read_file():
    from pathlib import Path
    # if not Path("test.txt").exists():
    test_file = Path("test.txt")
    if not test_file.exists():
        with open("test.txt","w") as f:
            f.write("test")

    with open("test.txt","r") as f:
        return {"content":f.read()}