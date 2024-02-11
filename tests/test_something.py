import pytest
import requests as rq
from config import PATH_URL


def test_getting_posts():
    response = rq.get(url=PATH_URL)
    assert response.status_code == 200, "Good req"
    print(response.text)
    pass
