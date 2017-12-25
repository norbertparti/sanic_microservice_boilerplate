import pytest

from server.main import app as my_app


@pytest.yield_fixture
def app():
    yield my_app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


async def test_hello(test_cli):
    """
    GET request
    """
    resp = await test_cli.get('/v1/hello')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"hello": 'world'}
