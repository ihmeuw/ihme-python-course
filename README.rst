Intro
=====

Schedule
--------

+--------------+--------------+----------------------+----------------------------------------------+
| Date         | Session      | Title                | Description                                  |
+==============+==============+======================+==============================================+
| Day 1        | Lecture 1    | Intro and Setup      | *Why Python, Setup, etc*                     |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 1        | Lecture 2    | Basic Python         | *Syntax, data structures, control flow, etc* |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 2        | Lecture 3    | Numpy + Pandas I     | *Numpy basics, series + dataframe basics*    |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 2        | Lecture 4    | Pandas II            | *Joining, advanced indexing, reshaping, etc* |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 2        | Lecture 5    | Pandas III + Plotting| *Grouping, intro to plotting, etc*           |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 3        | Lecture 7    | Intermediate Python  | *Writing and running program, debugging, etc*|
+--------------+--------------+----------------------+----------------------------------------------+
| Day 3        | Lecture 8    | Other Libraries      | *Intro to scipy, seaborn, etc*               |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 3        | Lecture 9    | Classes              | *Intro to object-oriented programming*       |
+--------------+--------------+----------------------+----------------------------------------------+

Getting started
===============

Clone this repo
---------------

First, you're going to want to get a copy of this repository onto your
machine. Simply fire up ``git`` and clone it:

1.  Open up a shell (e.g. ``cmd.exe`` or ``terminal.app``).

2.  Navigate to where you'd like to save this. We recommend ``~/repos/``
    (e.g. ``C:/Users/<user>/repos/`` on Windows, ``/Users/<user>/repos/``
    on Mac, or ``/home/<user>/repos/`` on Unix).

3.  Clone this repo:

    ::

        git clone https://github.com/IHME/ihme-python-course.git

Installing Anaconda
-------------------

The easy way
~~~~~~~~~~~~
Go to the `Anaconda download page <https://www.continuum.io/downloads>`_ and 
download the installer for Python 3.5 (64-bit) and simply click through to 
follow the instructions

The fancy way
~~~~~~~~~~~~~
If you'd like to setup a 
`Docker container with Anaconda <https://www.continuum.io/blog/developer-blog/anaconda-and-docker-better-together-reproducible-data-science>`_ 
check out the `Docker setup instructions <./Docker-Instructions.rst>`_. 
But be warned that it doesn't play terribly nicely with Windows 7 or 8...

Viewing slideshows
==================
The lectures are all Jupyter notebooks built with the 
[RISE](https://github.com/damianavila/RISE) live notebook presentation plugin. 
If you install RISE, you can view them as interactive slideshows (instead of
just notebooks). See the RISE page for more info, or simply:

::

    conda install -c damianavila82 rise

Acknowledgments
===============

Significant portions of this course were adapted from the following sources,
all of which are licensed under Creative Commons:

- `swcarpentry/python-novice-gapminder <https://github.com/swcarpentry/python-novice-gapminder>`_
- `TomAugspurger/pydata-chi-h2t <https://github.com/TomAugspurger/pydata-chi-h2t>`_
- `fonnesbeck/HealthPolicyPython <https://github.com/fonnesbeck/HealthPolicyPython/>`_
- `jrjohansson/scientific-python-lectures <https://github.com/jrjohansson/scientific-python-lectures>`_

License
=======
This work is licensed under a 
`Creative Commons Attribution 3.0 United States License <http://creativecommons.org/licenses/by/3.0/us/>`_.
