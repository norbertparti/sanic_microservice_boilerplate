from sanic import Sanic
from server.routes import bp

app = Sanic(__name__)

app.blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
