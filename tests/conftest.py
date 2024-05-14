import pytest
from starlette.testclient import TestClient

from tasks.main import app


@pytest.fixture(scope='session')
def test_app():
    with TestClient(app) as client:
        yield client
