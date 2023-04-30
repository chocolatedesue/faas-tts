from fastapi import FastAPI

from mangum import Mangum

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


handler = Mangum(app, lifespan="off")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)