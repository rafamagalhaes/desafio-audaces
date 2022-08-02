import pytest

from app import app


@pytest.fixture
def client():
    test_client = app.test_client()
    yield test_client


def test_challenge(client):
    response = client.get('/api/v1/challenge')
    assert b'Challenge accepted' in response.data
