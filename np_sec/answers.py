"""
These are answers to the questions in this part of the course.
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import os
from pathlib import Path
import sys
import timeit

import numpy as np

import gbd_example


LOGGER = logging.getLogger("answers")


def examine_input_data():
    years = gbd_example.years()
    age_groups = gbd_example.age_groups()
    lx = gbd_example.us_male_lx_one()
    qx = gbd_example.us_male_qx_one()

    LOGGER.info("All years: {}".format(", ".join(str(y) for y in years)))
    LOGGER.info("Age group count: {}".format(len(age_groups)))
    LOGGER.debug("lx males 2010 {}".format(lx))
    LOGGER.debug("qx males 2010 {}".format(qx))

    for idx in range(len(lx)):
        print(lx[idx], lx[idx] * qx[idx])


def compare_list_array():
    lx = gbd_example.us_male_lx_one()
    qx = gbd_example.us_male_qx_one()
    lx_np = np.array(lx)
    qx_np = np.array(qx)

    print("add lx {}".format(lx + lx))
    print("mult lx {}".format(lx * 3))
    print("add lx_np {}".format(lx_np + lx_np))
    print("mult lx_np {}".format(lx_np * 3))
    print("mult lx_np {}".format(lx_np * qx_np))


def deaths(lx, qx):
    deaths = list()
    for idx in range(len(lx)):
        deaths.append(lx[idx] * qx[idx])
    return deaths


def time_deaths():
    lx = gbd_example.us_male_lx_one()
    qx = gbd_example.us_male_qx_one()
    deaths_time = timeit.timeit(
        stmt="deaths(lx, qx)",
        globals=dict(lx=lx, qx=qx, deaths=deaths))
    print("Deaths takes {} s".format(deaths_time))


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", action="count", default=0)
    parser.add_argument("-q", action="count", default=0)
    args, _ = parser.parse_known_args()
    logging.basicConfig(level=logging.INFO - 10 * args.v + 10 * args.q)

    #examine_input_data()
    compare_list_array()
    #time_deaths()
