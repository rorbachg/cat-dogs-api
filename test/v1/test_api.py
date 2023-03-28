import json
import os

import numpy as np
import pytest
import requests

API_URL = f"{os.environ.get('APP_URL')}/v1/predict/"


@pytest.mark.parametrize(
    "url,class_",
    [
        (
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg",
            "Cat",
        ),
        (
            "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg",
            "Dog",
        ),
        (
            "https://assets-au-01.kc-usercontent.com/ab37095e-a9cb-025f-8a0d-c6d89400e446/33e0f89e-e666-4630-bed8-be87558a858f/article-cat-and-dog-skin-conditions-common.jpg",
            "Cat",
        ),
    ],
)
def test_model_single(url, class_):
    resp = json.loads(requests.post(API_URL, json={"urls": [url]}, timeout=10.0).text)

    assert resp.get("outputs")
    assert [key in ("names", "probabilities") for key in resp.get("outputs")[0].keys()]
    assert np.argmax(resp.get("outputs")[0].get("probabilities")) == 0 if class_ == "Cat" else 1


def test_model_multiple():
    resp = json.loads(
        requests.post(
            API_URL,
            json={
                "urls": [
                    "https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg",
                    "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2022-08/220805-border-collie-play-mn-1100-82d2f1.jpg",
                    "https://assets-au-01.kc-usercontent.com/ab37095e-a9cb-025f-8a0d-c6d89400e446/33e0f89e-e666-4630-bed8-be87558a858f/article-cat-and-dog-skin-conditions-common.jpg",
                ]
            },
            timeout=10.0,
        ).text
    )

    assert resp.get("outputs")
    assert len(resp.get("outputs")) == 3
    assert [key in ("names", "probabilities") for out in resp.get("outputs") for key in out]
