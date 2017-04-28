from sanic import Sanic
from sanic.response import text


app = Sanic()


@app.route('/ping')
async def ping(request):
    return text('pong')


@app.route('/task', methods=['POST'])
async def create_task(request):
    # Kick of a redis queue task
    return text('runnig', status=201)


@app.route('/task')
async def list_tasks(request):
    # list the pending tasks maybe
    return text('list of taks', status=200)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)