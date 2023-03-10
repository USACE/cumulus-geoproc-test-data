#!/usr/bin/python3
"""
Get the big files we can't store in the repo
"""

from datetime import datetime, timedelta
from pathlib import Path

import requests

FIXTURES = Path(__file__).parent.joinpath("fixtures")

yesterday = datetime.now() - timedelta(days=1)

BIG_GRIDS = {
    "hrrr-total-precip": [
        "https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.20220818/conus/hrrr.t00z.wrfsfcf00.grib2",
        "https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.20220818/conus/hrrr.t00z.wrfsfcf06.grib2",
    ],
    "nbm-co-01h": [
        yesterday.strftime(
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/00/core/blend.t00z.core.f001.co.grib2"
        ),
        yesterday.strftime(
            "https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.%Y%m%d/00/core/blend.t00z.core.f002.co.grib2"
        ),
    ],
}


def get_grids(acquire: dict):
    """get_grids"""
    for plugin, _urls in acquire.items():
        for _url in _urls:
            filename = Path(_url).name
            save_to = FIXTURES / plugin / filename
            req = requests.get(_url, timeout=30, stream=True)
            with save_to.open("wb") as fptr:
                for chunk in req.iter_content(chunk_size=1024):
                    if chunk:
                        fptr.write(chunk)


if __name__ == "__main__":
    get_grids(BIG_GRIDS)
