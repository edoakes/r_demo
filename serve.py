#!/usr/bin/env python

from fastapi import FastAPI

import ray
from ray import serve

from utils import connect_to_ray

app = FastAPI()

@serve.deployment(route_prefix="/", num_replicas=4)
@serve.ingress(app)
class MyApp:
    @app.get("/")
    def say_hello(self, name: str):
        return f"Hello {name}!"

if __name__ == "__main__":
    connect_to_ray()
    serve.start(detached=True)

    print("Deploying!")
    MyApp.deploy()
    print("Deploying succeeded.")
