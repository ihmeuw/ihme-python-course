"""
This is a file in which to work.
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import sys
import timeit


LOGGER = logging.getLogger("working")


def examine_input_data():
    pass


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("-v", action="count", default=0,
                        help="Add -v to increase verbosity.")
    parser.add_argument("-q", action="count", default=0,
                        help="Add -q to quiet logging.")
    args, _ = parser.parse_known_args()
    logging.basicConfig(level=logging.INFO - 10 * args.v + 10 * args.q)

    examine_input_data()
