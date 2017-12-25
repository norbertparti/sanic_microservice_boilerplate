import aiohttp


from sanic import Blueprint, response
from sanic.response import json

apiVersionOne = Blueprint('v1', url_prefix='/v1')


async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with session.get(url) as session:
        return await session.json()


@apiVersionOne.route("/")
async def test(request):
    """
    Download and serve example JSON
    """
    url = "https://api.github.com/repos/channelcat/sanic"

    async with aiohttp.ClientSession() as session:
        res = await bounded_fetch(session, url)
        return json(res)


@apiVersionOne.route("/hello")
async def hello(request):
    return response.json({"hello": "world"})
