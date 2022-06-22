from flask import Flask
import redis

app = Flask(__name__)
app.config.from_prefixed_env()
redis_host = app.config.get('REDIS_HOST', 'localhost')
redis_client = redis.from_url(f'redis://{redis_host}:6379')

@app.route('/')
def hello():
    if redis_client.get('visitors') is None:
        redis_client.set('visitors', 0)
    visitors = redis_client.incr('visitors')
    return f'<h1>This is the {visitors} visitor></h1>'
