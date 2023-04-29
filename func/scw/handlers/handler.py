from mangum import Mangum
from app import app 


handler = Mangum(app, lifespan="off")

# dir(handler)
if __name__ == "__main__":
    print(dir(handler))
    print(handler.__dict__)