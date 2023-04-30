from mangum import Mangum
from app import app 


handler = Mangum(app, lifespan="off")

# dir(handler)
if __name__ == "__main__":
    # print(dir(handler))
    # print(handler.__dict__)
    import uvicorn
    uvicorn.run(
        app, host='0.0.0.0',port=8000
    )