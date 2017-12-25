from sanic import Sanic
from server.routes import bp

app = Sanic(__name__)

app.blueprint(bp)

app.run(host="0.0.0.0", port=8000, workers=2)
