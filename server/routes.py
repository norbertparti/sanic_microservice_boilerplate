from sanic.response import json
from sanic import Blueprint, response

import aiohttp

bp = Blueprint('v1', url_prefix='/v1')

async def bounded_fetch(session, url):
    """
    Use session object to perform 'get' request on url
    """
    async with session.get(url) as session:
        return await session.json()


@bp.route("/")
async def test(request):
    """
    Download and serve example JSON
    """
    url = "https://api.github.com/repos/channelcat/sanic"

    async with aiohttp.ClientSession() as session:
        res = await bounded_fetch(session, url)
        return json(res)


@bp.route("/hello")
async def hello(request):
    return response.json({"hello": "world"})
