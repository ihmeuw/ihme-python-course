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
| Day 3        | Lecture 5    | Pandas III           | *Grouping, apply, transform, etc*            |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 3        | Lecture 6    | Plotting             | *Intro to plotting in Python*                |
+--------------+--------------+----------------------+----------------------------------------------+
| Day 3        | Lecture 7    | Regression Intro     | *Intro to regressions with Statsmodels*      |
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

Saving local changes
--------------------

You probably want to take notes, etc in your notebooks, so it's best to either
fork this repo or just make a local branch to work off of:

1. Use `git checkout` to make a new branch

    ::

        git checkout -b my_branch_name

2. Save any changes using `git add` and then `git commit`

    ::

        git add .
        git commit -m "describe your change"

3. To get updates from the master branch, first fetch them:

    ::

        git fetch

4. Then apply the changes from master to your personal branch:

    ::

        git merge origin/master



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

Additional modules
~~~~~~~~~~~~~~~~~~

- `seaborn <https://seaborn.github.io>`_
    
    ::

        conda install -c conda-forge seaborn

- `ggplot <http://ggplot.yhathq.com/>`_

    ::

        conda install -c bokeh ggplot

- `bokeh <http://bokeh.pydata.org/en/latest/>`_

    ::

        conda install -c bokeh bokeh

- `statsmodels <http://statsmodels.sourceforge.net/>`_

    ::

        conda install -c conda-forge statsmodels


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
