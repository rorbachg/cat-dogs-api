from typing import List

from pydantic import BaseModel


class ItemResp(BaseModel):
    names: List[str]
    probabilities: List[float]


class Item(BaseModel):
    urls: List[str]

    class Config:
        schema_extra = {
            "example": {
                "urls": [
                    "https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg",
                    "https://cdn.britannica.com/86/166986-050-4CEFE5DE/cute-kitten-and-puppy-outdoors-in-grass.jpg",
                    "https://assets-au-01.kc-usercontent.com/ab37095e-a9cb-025f-8a0d-c6d89400e446/33e0f89e-e666-4630-bed8-be87558a858f/article-cat-and-dog-skin-conditions-common.jpg",
                ]
            }
        }


class Resp(BaseModel):
    outputs: List[ItemResp]

    class Config:
        schema_extra = {
            "example": {
                "outputs": [
                    {"names": ["Cat", "Dog"], "probabilities": [0.9999, 0.0001]},
                    {"names": ["Cat", "Dog"], "probabilities": [0.0003, 0.9997]},
                    {"names": ["Cat", "Dog"], "probabilities": [0.845, 0.155]},
                ]
            }
        }
