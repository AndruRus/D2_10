import os
import sentry_sdk

from bottle import route, run, HTTPError, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://986303b801c94128a4d060353238b45a@o496969.ingest.sentry.io/5572405",
    integrations=[BottleIntegration()]
)

@route("/")
def main():
    result = HTTPResponse(status=200, body="OK")
    return result

@route("/success")
def success():
    result = HTTPResponse(status=200, body="200 OK")
    return result

@route("/fail")
def fail():
    raise RuntimeError("There is an error!")

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
