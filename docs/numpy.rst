=====
Numpy
=====


Exercise 1: Calculate Deaths
----------------------------

We will work with data directly from the GBD outputs for overall
population and mortality for countries. These are life tables for
populations, where each population is classified by

 * ``location_id``, which indicates country or district within a country.
   China is 6. The United States is 102.

 * ``year_id`` the year for which we have this data.

 * ``sex_id``, which is 1 for male, 2 for female, 3 for both sexes.

 * ``age_group_id``, which is an identifier for each age interval. These
   tend to be smaller for the young, so 28 is the first year,
   5 is the next four years, and 6, onward are 5-year age intervals
   ending with a half-open interval to account for Jeanne Calment,
   who lived to 122 years, 164 days.

The two values we read
are

.. math::

   l_x = \mbox{population at start of age interval}

   {}_nq_x = \mbox{fraction that die within age interval}

   {}_nq_x = P[X\le x+n|X>x]

Let's take a look at that data. We'll need some functions that are
provided for you.

.. autofunction:: np_sec.gbd_example.years

.. autofunction:: np_sec.gbd_example.age_groups

.. autofunction:: np_sec.gbd_example.us_male_lx_one

.. autofunction:: np_sec.gbd_example.us_male_qx_one

.. autofunction:: np_sec.gbd_example.us_male_lx

.. autofunction:: np_sec.gbd_example.us_male_lx

Question 1:
^^^^^^^^^^^
Write a script that imports ``gbd_example`` and
prints

 * the number of age groups the GBD uses
 * the years covered
 * lx for US males in 2010
 * qx for US males in 2010

