from sanic import Sanic
from sanic.response import text


app = Sanic()


@app.route('/ping')
async def ping(request):
    return text('pong')


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)