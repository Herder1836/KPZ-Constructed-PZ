from flask import Flask
import redis, os

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f"Hello from Docker! This page has been viewed {count} times."

if __name__ == '__main__':
    port = int(os.environ.get('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
