from typing import Optional

import requests

import typer

app = typer.Typer()

URL = "https://ci-f676382eb1183178a8038fa710bc0aa2d8606387.anyscale-dev.dev/ext/v0/ha_jobs/submit"
COOKIES = {
    "sessionv2": "sss_h9YHN4KkGsSPSnQkZYj3624b",
    "io": "f907a671bcc74cf19efd9a2ae35813ca"
}

@app.command()
def submit(package: str, entrypoint: str, name: Optional[str] = "test_job"):
    requests.post(URL, cookies=COOKIES, json={
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

@app.command()
def status():
	pass

if __name__ == "__main__":
    app()
