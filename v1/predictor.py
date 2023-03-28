from io import BytesIO
from typing import Any

import httpx
import tensorflow as tf

from .models import ItemResp


class Predictor:
    def __init__(self, model_path: str) -> None:
        self.model = tf.keras.models.load_model(model_path)
        self.labels = ["Cat", "Dog"]

    @staticmethod
    def read_image(content: bytes, input_height: int, input_width: int) -> Any:
        image = tf.keras.preprocessing.image.load_img(BytesIO(content), target_size=(input_height, input_width))
        image_p = tf.keras.preprocessing.image.img_to_array(image)
        image_p = image_p.reshape((1, image_p.shape[0], image_p.shape[1], image_p.shape[2]))
        image_p = tf.keras.applications.resnet.preprocess_input(image_p)

        return image_p

    async def transform(self, url: str) -> ItemResp:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        content = response.read()
        image = self.read_image(
            content,
            input_height=self.model.input_shape[1],
            input_width=self.model.input_shape[2],
        )
        pred = self.model(image)
        out = ItemResp(
            names=self.labels,
            probabilities=pred[0].numpy().round(4).astype(str).tolist(),
        )
        return out
