import ray
import time


@ray.remote
def sleep(time_period):
    time.sleep(time_period)
    return "done"


ray.init("auto")
sleep_for = 1
print(ray.get(sleep.remote(sleep_for), timeout=sleep_for + 30))
