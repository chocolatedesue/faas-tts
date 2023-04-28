import logging
import azure.functions as func
from app import app  # Main API application
# import text 


# @app.get("/sample")
# async def index():
#     return {
#         "info": "Try /hello/Shivani for parameterized route.",
#     }


# @app.get("/hello/{name}")
# async def get_name(name: str):
#     return {
#         "name": name,
#     }


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
