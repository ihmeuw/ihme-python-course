=====
Numpy
=====


Exercise 1: Calculate Deaths
----------------------------

Background on GBD Output
^^^^^^^^^^^^^^^^^^^^^^^^

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
   ending with a half-open interval to account for
   `Jeanne Calment <https://en.wikipedia.org/wiki/Oldest_people>`_,
   who lived to 122 years, 164 days.

The two values we read
are

.. math::

   l_x = \mbox{population at start of age interval}

   {}_nq_x = \mbox{fraction that die within age interval}

If we think of each individual as dying at a random time :math:`X`,
then :math:`{}_nq_x` is the probability that they die by the end
of the interval given that they lived to the start of the interval,

.. math::

   {}_nq_x = P[X\le x+n|X>x]

Let's take a look at that data. We'll need some functions that are
provided for you.

.. autofunction:: gbd_example.years

.. autofunction:: gbd_example.age_groups

.. autofunction:: gbd_example.us_male_lx_one

.. autofunction:: gbd_example.us_male_qx_one

.. autofunction:: gbd_example.us_male_lx

.. autofunction:: gbd_example.us_male_lx

Python format function help at `Python site <https://docs.python.org/3/tutorial/inputoutput.html>`_
and the `formatting site. <https://pyformat.info/>`_

Logging
^^^^^^^
Logging is a way to add messages to the code that are a secondary
stream of information, besides what you print or write to disk.
For example::

   LOGGER = logging.getLogger("myfile")
   logging.basicConfig(level=logging.INFO)

   LOGGER.info("Going to write the file gbd_out.nc")
   LOGGER.debug("The data starts with {}".format(data[0:10]))
   if all_wrong:
       LOGGER.error("Gone wrong, and this is the situation: {}".format(3))
       exit()

================  ==================================================
Call              When to use it
================  ==================================================
LOGGER.debug      Messages that help see if code runs.
LOGGER.info       Things users normally need to see.
LOGGER.warn       Something's likely going wrong.
LOGGER.error      Something's wrong and we'll exit.
LOGGER.exception  Something's wrong and the exception says more.
================  ==================================================

The ``basicConfig`` call sets which level will print when the job runs.



Question 1: Examine Input Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Write a script that imports ``gbd_example`` and
prints

 * the number of age groups the GBD uses
 * the years covered
 * Use a loop over the arrays to print two values,
   :math:`l_x` for US males in 2010 and
   :math:`{}_nq_x\:\times\:l_x` for US males in 2010.
   You will need to create a loop index that runs from 0 to the
   length of the :math:`l_x` array.

Do you see a pattern in the columns? The second column is the
number of deaths each year, called :math:`{}_nd_x = {}_nq_x\:l_x`.

Conversion to a Numpy Array
---------------------------

Creation of Numpy Arrays
^^^^^^^^^^^^^^^^^^^^^^^^
To convert a list to a numpy array::

   import numpy as np
   a = [1.4, 2.7, 3.2]
   a_np = np.array(a)

To create a numpy array full of zeros or ones::

   import numpy as np
   a = np.zeros((24,))
   b = np.ones((42,))


Algebraic Operators in Numpy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   import numpy as np
   a = np.array([1.4, 2.7, 3.1])
   b = np.array([2.3, 4.7, 6.9])
   c = a + b
   d = a * b
   e = a / b


Question 1: Algebraic Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 1. Make a new function. Store ``us_male_lx_one()`` in ``lx``
    and ``us_male_qx_one()`` in ``qx``.

 2. Find the value of the following::

       lx + lx
       lx * 6

    What does each of those operations do?

 3. Convert them to Numpy arrays named ``lx_np`` and ``qx_np``. Try the following::

       lx_np + lx_np
       lx_np * 3
       lx_np * qx_np

 4. How do numpy arrays behave differently from lists? This behavior
    is called a "pointwise" or "elementwise" operation. Statisticians
    call the multiplicative version the
    `Hadamard product <https://en.wikipedia.org/wiki/Hadamard_product_(matrices)>`_
    because they like to think they invent things.


Exercise 3: Numpy Data Structure, Data Types
--------------------------------------------

The Array Object
^^^^^^^^^^^^^^^^
A numpy array object has members and methods. The two most important
are the shape and dtype::

    >>> a=np.array([1,2,17,4])
    >>> a.shape
    (4,)
    >>> len(a)
    4
    >>> a.dtype
    dtype('int64')
    >>> a.data
    <memory at 0x7f6aa45ce7c8>

The ``data`` member is where numpy stores the numbers 1, 2, 3, 4
in a highly-efficient format. We can't access them except through the
accessor, much like lists::

    >>> print(a[2])
    17
    >>> a[1] = 81
    >>> print(a)
    [1 81 17 4]
    >>> print(a[1:3])
    [2 17]
    >>> print(a[:3])
    [1 2 17]


Data Types
^^^^^^^^^^
The Python language defines a set of types, which include::

    >>> type("hiya")
    <class 'str'>
    >>> type(3)
    <class 'int'>
    >>> type(3.3)
    <class 'float'>
    >>> type(True)
    <class 'bool'>
    >>> type(None)
    <class 'NoneType'>
    >>> type(object())
    <class 'object'>

It also defines conversions among those types::

   >>> float(3)
   3.0
   >>> int(True)
   1
   >>> bool(11)
   True

The numpy type system is much more precise about
`numbers <https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.scalars.html>`_,
and every value in the array must have the same type.

=========  =================================================================
dtype      Use
=========  =================================================================
np.int8    An 8-bit integer, represents -128 to 128.
np.int     This is always an alias for an integer the size of Python's int.
np.float   This is an alias for a real number the size of Python's float.
np.single  A real number with 8 bytes of information, very rarely used.
np.double  A real number with 16 bytes, our default.
np.bool    This is an alias for a PPython bool.
=========  =================================================================

The numbers are called dtypes because they are most often used
when creating arrays like this::

   lx = np.ones((24,), dtype=np.float)
   age_group_id = np.zeros((24,), dtype=np.int)

Numpy arrays convert all at once::

   lx_ieee = lx.astype(np.double)
   lx_int = lx.astype(np.int)

Converting from a float to an integer truncates the fractional part.


Question 1: Array Type
^^^^^^^^^^^^^^^^^^^^^^

 1. Create an array called ``desc`` containing all integers, such as [17, 32, 3, 1],
    and convert it to a Numpy array of type ``np.int``.

 2. What is the ``type`` of that array? What is the ``type`` of the
    second value in the array? Does adding 3 to it change the type?

 3. Try using the second value in the array in a range statement.
    Does that work::

       print(list(range( desc[1] )))

 4. Multiply the array created in the last problem by 3.14 and assign the result
    to a new value. What's the ``dtype`` of that array?

 5. We know that we can add, subtract, multiply, and divide. What do
    the less-than (<) and greater-than (>) operators do? Take the array
    from above and try ``desc < 16``. What is the ``dtype`` of the result?
    Now look at ``desc[desc<16]``.

    *More* Try ``desc[np.sin(desc) < 0.8]``. Print each step taken to evaluate
    this statement.

 6. Convert the float array to integers. Then subtract the integers
    from the floating array in order to find the fractional parts.
    What type is the result?


Selection Within Arrays
-----------------------
bit vectors
all and any



Exercise 2: Timing, Sizes
-------------------------

Dictionaries
^^^^^^^^^^^^
A `dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
is a data structure that maps keys to values.
The keys have to be immutable, and the values can be any object.

There are several ways to create a dictionary::

   empty_dict = dict()
   pop_map = { 28: 100000, 5: 999966 }
   coords = dict(year_id=[1990, 1991], sex_id=[1, 2, 3])
   coords = {"year_id": [1990, 1991], "sex_id": [1, 2, 3]}

The last two lines do the same thing.
Once you make it, entries can be read or added with item accessors,::

   print(coords["year_id"])
   pop_map[6] = 999700


Timing with ``timeit``
^^^^^^^^^^^^^^^^^^^^^^
The built-in `timeit module <https://docs.python.org/3/library/timeit.html?highlight=timeit#module-timeit>`_
can tell us how long it takes for a statement to run.
Calling ``timeit.timeit`` can be a challenge. For instance, assume
we have already defined a ``deaths`` function that multiplies
:math:`l_x` and :math:`q_x`. Then we time it::

    def deaths(lx, qx):
        return lx[0] * qx[0]

    def time_deaths():
        lx = gbd_example.us_male_lx_one()
        qx = gbd_example.us_male_qx_one()
        deaths_time = timeit.timeit(
            stmt="deaths(lx, qx)",
            globals=dict(lx=lx, qx=qx, deaths=deaths))
        print("Deaths takes {} s".format(deaths_time))

The ``timeit`` function denies that the variables ``lx``, ``qx``,
and ``deaths`` are defined unless you give it the ``globals`` argument,
which is a dictionary where the keys are the variables and functions
the timing statement (``stmt``) needs to run.
Do you see the ``dict`` definition style used? Python knows, when it
sees ``dict(lx=lx)`` that it is supposed to create a dictionary
entry where the key is the string ``"lx"`` and the value is the
list of numbers from the variable ``lx``.


Find the Size of a Python Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is a Python function that tells you how much memory
an object uses. It's the function ``getsizeof`` in the ``sys`` module,
so it's called with::

   import sys

   def make_something():
       a = [100000, 99877, 89777]
       a_size_in_bytes = sys.getsizeof(a)
       print("a bytes {}".format(a_size_in_bytes))

Sizes of data in memory or on disk have the units:

=========   ==============    =============================================
Unit        Abbreviation      Size
=========   ==============    =============================================
Byte        B                 Represents a number between 0 and 256
Kilobyte    kB                1024 Bytes
Megabyte    MB                1024 KB, approximately :math:`10^6` Bytes
Gigabyte    GB                1024 MB, approximately :math:`10^9` Bytes
Terabyte    TB                1024 GB, approximately :math:`10^{12}` Bytes
=========   ==============    =============================================


Question 2: Memory Usage
^^^^^^^^^^^^^^^^^^^^^^^^

 1. Find the size in memory of a Python list for :math:`l_x`.
    Compare it with the size of the Numpy array for :math:`l_x`.

 2. *More* Make a new list that's a hundred times longer for each.
    Again, find the size.



Collective Operations
---------------------

A collective operation is an operation on a set of things.
This is not a collective operation::

   lx_np = np.array(gbd_example.us_male_lx_one())
   for lx in range(1, len(lx_np)):
        dx = lx[idx] - lx[idx-1]

This is a collective operation::

   dx = lx[:-1] - lx[1:]

In the language of Python, a ``ufunc`` is a function that acts
elementwise on an array. For instance, we can's use Python's ``sin``
function to get the sine of values, but numpy defines a ``ufunc``
version we can use::

   import math
   import numpy as np

   arr = np.array([0.9, 0.7, 0.6], dtype=np.float)
   try:
       result = sin(arr)
   except TypeError as te:
       print("Cannot get the sin of an array using built-in sin")

   # But the numpy version is a ufunc, so it applies across all.
   print(np.sin(arr))


Scipy Library
^^^^^^^^^^^^^
Numpy is the common language for almost all Python mathematics.
Using it gives you access to
`Scipy <https://docs.scipy.org/doc/scipy/reference/>`_, which has a wide range
of computational functions. Many operations in Scipy are ufuncs.

