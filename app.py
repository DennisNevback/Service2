from flask import Flask
import requests
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info("app_info", "Application_info", version="1.0.3")


@app.route('/')
def hello_world():
    r = requests.get("http://service2-service1-1:5001")
    return f"Hello from service2. Service 1 says: {r.text}"


app.run(host="0.0.0.0", port=5002, debug=True)
