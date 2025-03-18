import uvicorn
from multiprocessing import Process

import auth_service
import auth_service_db
import backgammon_core
import backgammon_core_db
import gateway
import web_site


workers = 2


def run_auth_service():
    uvicorn.run("auth_service:app", host="127.0.0.1", port=auth_service.port, workers=workers)


def run_auth_service_database():
    uvicorn.run("auth_service_db:app", host="127.0.0.1", port=auth_service_db.port, workers=workers)


def run_backgammon_core():
    uvicorn.run("backgammon_core:app", host="127.0.0.1", port=backgammon_core.port, workers=workers)


def run_backgammon_core_database():
    uvicorn.run("backgammon_core_db:app", host="127.0.0.1", port=backgammon_core_db.port, workers=workers)


def run_gateway_service():
    uvicorn.run("gateway:app", host="127.0.0.1", port=gateway.port, workers=workers)


def run_web():
    uvicorn.run("web_site:app", host="127.0.0.1", port=web_site.port, workers=workers)


services = [run_auth_service, run_auth_service_database,
            run_backgammon_core, run_backgammon_core_database,
            run_gateway_service,
            run_web]


def main():
    Process(target=run_auth_service_database).start()
    Process(target=run_auth_service).start()
    # Process(target=run_web).start()
    # for service in services:
    #     Process(target=service).start()
    return


if __name__ == "__main__":
    main()
