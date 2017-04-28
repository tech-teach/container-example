import time

from sanic import Sanic
from sanic.response import text
from rq import Queue
from redis import Redis

redis_conn = Redis(host='queue')
q = Queue(connection=redis_conn)

app = Sanic()


def sleepear():
    time.sleep(5)

@app.route('/ping')
async def ping(request):
    return text('pong')


@app.route('/task', methods=['POST'])
async def create_task(request):
    # Kick of a redis queue task
    q.enqueue('app.sleepear')
    return text('runnig', status=201)


@app.route('/task')
async def list_tasks(request):
    # list the pending tasks maybe
    return text(
        str(q.count),
        status=200
    )


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)