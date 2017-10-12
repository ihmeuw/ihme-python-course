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


def us_male_np():
    """
    Returns :math:`l_x` and :math:`{}_nq_x` as numpy arrays.

    Returns:
         Tuple containing lx, qx.
    """
    lx = gbd_example.us_male_lx_one()
    qx = gbd_example.us_male_qx_one()

    # Convert them to numpy arrays

    # And return them both
    return (lx_np, qx_np)


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
