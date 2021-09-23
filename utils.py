import os

import ray

def connect_to_ray():
    job_config = ray.job_config.JobConfig()
    job_config.set_metadata("creator_id", "usr_QiSM2sZG7uK8UaA8EuFpLker")

    if os.getenv("ANYSCALE_SESSION_ID") is not None:
        address = "auto"
    else:
        address = None

    ray.init(address=address, job_config=job_config)
