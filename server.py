#Импортируем библиотеки

import os
import sentry_sdk

from bottle import route, run, HTTPError, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

#подключаем sentry
sentry_sdk.init(
    dsn="sentry_dsn",
    integrations=[BottleIntegration()]
)

#реализуем отображение
#статус ОК
@route("/")
def main():
    result = HTTPResponse(status=200, body="200 OK")
    return result

@route("/success")
def success():
    result = HTTPResponse(status=200, body="200 OK")
    return result

#статус ошибка
@route("/fail")
def fail():
    raise RuntimeError("There is an error!")

#настройка отображения в heroku или локально
if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
