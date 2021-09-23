#!/usr/bin/env python

from pprint import pprint
from typing import Optional

import requests

import typer

app = typer.Typer()

SUBMIT_URL = "https://ci-f676382eb1183178a8038fa710bc0aa2d8606387.anyscale-dev.dev/ext/v0/ha_jobs/submit"
KILL_URL = "https://ci-f676382eb1183178a8038fa710bc0aa2d8606387.anyscale-dev.dev/ext/v0/ha_jobs/{job_id}/kill"
GET_URL = "https://ci-f676382eb1183178a8038fa710bc0aa2d8606387.anyscale-dev.dev/ext/v0/ha_jobs/{job_id}"
COOKIES = {
    "sessionv2": "sss_h9YHN4KkGsSPSnQkZYj3624b",
    "io": "f907a671bcc74cf19efd9a2ae35813ca"
}

@app.command()
def submit(package: str, entrypoint: str, name: Optional[str] = "test_job"):
    print(f"Submitting job package='{package}' :: entrypoint='{entrypoint}'")
    r = requests.post(SUBMIT_URL, cookies=COOKIES, json={
      "name": name,
      "entrypoint": entrypoint,
      "runtime_env": {
        "name": "string",
        "working_dir": package
      },
      "build_id": "bld_Mxt8aGbnFsnHMDUtadhXVuMB",
      "compute_template_id": "cpt_T3EbHvqFUgdcH2xUA5NQAfay",
      "max_retries": 5
    })
    print("\nSubmitted job successfully, response:")
    response = r.json()
    del response["result"]["job_id"]
    del response["result"]["state"]
    pprint(response)

@app.command()
def stop(job_id: str):
    print(f"Killing job '{job_id}'")
    r = requests.get(KILL_URL.format(job_id=job_id), cookies=COOKIES)
    print("\nKilled job successfully, response:")
    pprint(r.json())

@app.command()
def status(job_id: str):
    print(f"Getting job status for job '{job_id}'")
    r = requests.get(GET_URL.format(job_id=job_id), cookies=COOKIES)
    print("\nResponse:")
    pprint(r.json())

if __name__ == "__main__":
    app()
