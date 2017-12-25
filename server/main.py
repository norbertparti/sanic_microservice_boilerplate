from sanic import Sanic

from server.routes import apiVersionOne

app = Sanic(__name__)

app.blueprint(apiVersionOne)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
