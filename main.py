import asyncio
import os
from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from v1.models import Item, Resp
from v1.predictor import Predictor


def custom_openapi() -> Optional[Dict[str, Any]]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Cats and Dogs API",
        version="1.0.0",
        description="This is a documentation for cats and dogs classification API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {"url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()
api_v1 = FastAPI()
app.mount("/v1", api_v1)
app.openapi = custom_openapi

model_path = os.environ.get("MODEL_PATH")
predictor = Predictor(model_path)


@api_v1.post("/predict/")
async def predict(item: Item) -> Resp:
    coros = [predictor.transform(url) for url in item.urls]
    outputs = await asyncio.gather(*coros)
    return Resp(outputs=outputs)
