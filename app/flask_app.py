import time
import random

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

my_counter = metrics.counter('by_code_counter', 'Request count by code',
                             labels={'path': lambda: request.path, 'status': lambda r: r.status_code})


@app.route('/one')
@my_counter
def first_route():
    time.sleep(random.random() * 0.2)
    return 'ok'


@app.route('/two')
def the_second():
    time.sleep(random.random() * 0.4)
    return 'ok'


@app.route('/three')
def test_3rd():
    time.sleep(random.random() * 0.6)
    return 'ok'


@app.route('/four')
def fourth_one():
    time.sleep(random.random() * 0.8)
    return 'ok'


@app.route('/error')
def oops():
    return ':(', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
