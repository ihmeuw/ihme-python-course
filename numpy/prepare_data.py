"""
This script converts GBD output into a format suitable for the course.
It relies on methods and libraries not discussed within the course.
The GBD output was read earlier by a script that reads db_queries
and produces XArray versions of that data.
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import os
from pathlib import Path

from jinja2 import Template
import numpy as np
import xarray as xr

import fbd_core.demog


LOGGER = logging.getLogger("ihme_python_course.numpy.prepare_data")
GBDDATA = Path("/ihme/forecasting/data/4/past/"
               "life_expectancy/20171006_shock_hiv")

def translate_data(gbd_path):
    """
    Reads input data files and outputs Python data structures.
    The postcondition is that those files will be sorted according
    to the age at which age intervals begin, so they will be in age order.

    :param gbd_path:
    :return: A dictionary of lx, qx.
    """
    qx_file = gbd_path / "gbd_qx.nc"
    lx_file = gbd_path / "gbd_lx.nc"
    LOGGER.info("opening files {} {}".format(qx_file, lx_file))
    qx_xr = xr.open_dataarray(str(qx_file))
    lx_xr = xr.open_dataarray(str(lx_file))
    age_ids = lx_xr.age_group_id.values.copy()
    # Incoming data usually has the youngest age group out of order.
    # 28 is the youngest age group, so move it to front.
    LOGGER.debug("age_ids in {}".format(age_ids))
    loc28 = np.where(age_ids == 28)[0][0]
    LOGGER.debug("loc of 28 {}".format(loc28))
    age_ids[loc28] = 1
    would_sort = age_ids.argsort()
    age_sort = lx_xr.age_group_id.values[would_sort]
    LOGGER.debug("would sort {}".format(would_sort))
    lx_sort = lx_xr.loc[dict(age_group_id=age_sort)]
    LOGGER.debug("age_ids in qx {}".format(qx_xr.age_group_id.values))
    a = set(qx_xr.age_group_id.values)
    b = set(lx_xr.age_group_id.values)
    LOGGER.debug("qx lx diff {} {}".format(a - b, b - a))
    qx_sort = qx_xr.loc[dict(age_group_id=age_sort)]
    return {"lx": lx_sort, "qx": qx_sort}


def choose_inputs(gbd_data):
    """
    Creates a Python module that contains data in a simple list
    format.

    :param gbd_data:
    :return:
    """
    template = Template(open("gbd_example.jinja", "r").read())
    lx = gbd_data["lx"]
    us_men_2010 = dict(location_id=102, sex_id=1, year_id=2010)
    vals = dict()
    vals["us_male_lx_2010"] = list(lx.loc[us_men_2010].values)
    us_men = dict(location_id=102, sex_id=1)
    vals["us_male_lx"] = list(list(y) for y in lx.loc[us_men].T.values)
    vals["years"] = list(lx.year_id.values)
    vals["age_group"] = list(lx.age_group_id.values)
    qx = gbd_data["qx"]
    vals["us_male_qx_2010"] = list(qx.loc[us_men_2010].values)
    vals["us_male_qx"] = list(list(y) for y in qx.loc[us_men].T.values)

    with open("gbd_example.py", "w") as gbd_out:
        gbd_out.write(template.render(**vals))
        gbd_out.write(os.linesep)


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", action="count", default=0)
    parser.add_argument("-q", action="count", default=0)
    parser.add_argument("--input", type=Path, help="Directory with input data",
                        required=False, default=GBDDATA)
    args, _ = parser.parse_known_args()
    logging.basicConfig(level=logging.INFO - 10 * args.v + 10 * args.q)

    local_path = Path("./data")
    if args.input.exists():
        input_path = args.input
    elif local_path.exists():
        input_path = local_path
    else:
        raise RuntimeError("Cannot find input path {}".format(args.input))

    arrays = translate_data(input_path)
    choose_inputs(arrays)