"""
This is a file in which to work.
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import logging
import sys
import timeit


LOGGER = logging.getLogger("working")


def examine_input_data():
    # Get lx and qx from our input module, gbd_example.

    # Create a list into which to put the results

    # Loop over the arrays, and store into the result list

    # print the result list
    LOGGER.debug("examine_input_data begin")


def calculate_death(lx, qx):
    """
    Given population and mortality, return the deaths for each interval.

    Arguments:
          lx (list[float]): :math:`l_x`, population at start of each interval
          qx (list[float]): :math:`{}_nq_x`, mortality over each interval

    Returns:
          list[float]: :math:`d_x = l_x\:{}_nq_x` deaths
    """
    return dx


def test_calculate_death():
    dx = calculate_death(gbd_example.us_male_lx_one(),
                         gbd_example.us_male_qx_one())
    assert np.allclose(dx, gbd_example.us_male_dx_one())


def calculate_death_np(lx, qx):
    """
    Given population and mortality, return the deaths for each interval.

    Arguments:
          lx (np.array): :math:`l_x`, population at start of each interval
          qx (np.array): :math:`{}_nq_x`, mortality over each interval

    Returns:
          list[float]: :math:`d_x = l_x\:{}_nq_x` deaths
    """
    return dx


def us_male_np():
    """
    Returns :math:`l_x` and :math:`{}_nq_x` as numpy arrays.

    Returns:
         Tuple containing lx, qx.
    """
    # Get lx and qx from our input module, gbd_example.

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
