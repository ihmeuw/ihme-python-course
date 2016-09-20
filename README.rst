Intro
=====

Lorem ipsum

Goals
-----

This course will teach you...

Schedule
--------

+--------------+---------------------+----------------------------------------------+
| Session      | Title               | Description                                  |
+==============+=====================+==============================================+
| Lecture 1    | Setup               | Installation, Jupyter notebooks              |
+--------------+---------------------+----------------------------------------------+
| Lecture 2    | Basic Python        | Syntax, data structures, control flow, etc   |
+--------------+---------------------+----------------------------------------------+
| Exercise 1   | My First Notebook   | ...                                          |
+--------------+---------------------+----------------------------------------------+
| Lecture 3    | Pandas I            | Reading data, dataframe basics               |
+--------------+---------------------+----------------------------------------------+

Getting started
===============

In order to make sure everyone is operating off of the same page, we're
going to be using `Docker <https://www.docker.com/what-docker>`_ and
`Anaconda <https://www.continuum.io/anaconda-overview>`_ to setup
consistent Python development environments.

Please follow the installation instructions for Docker and Anaconda
below to make sure you have a working Python environment prior to the
beginning of the course.

Clone this repo
---------------

First, you're going to want to get a copy of this repository onto your
machine. Simply fire up ``git`` and clone it:

1. Open up a shell (e.g. ``cmd.exe`` or ``terminal.app``).

2. Navigate to where you'd like to save this. We recommend ``~/repos/``
   (e.g. ``C:/Users/<user>/repos/`` on Windows, ``/Users/<user>/repos/``
   on Mac, or ``/homes/<user>/repos/`` on Unix).

3. Clone this repo:

   ::

       git clone git@github.com:IHME/ihme-python-course.git

Install Docker
--------------

Docker enables you to create "containers" which provide consistent
environments in which to run your code. This way, you can run the
software you write on different machines (e.g. your laptop vs the
computing cluster) without having to spend too much time worrying about
adapting it.

We're going to just be using some very basic features of Docker, so if
you'd like to learn more refer to `this
page <https://docs.docker.com/engine/understanding-docker/>`__.

Windows 10
~~~~~~~~~~

Detailed installation instructions are available
`here <https://docs.docker.com/docker-for-windows/>`_. For our
purposes, you can simply:

1. `Download <https://download.docker.com/win/stable/InstallDocker.msi>`_
   the installer.

2. Double click on the installer and follow the prompts (keeping all
   options as defaults is fine).

3. Open a shell (e.g. ``cmd.exe``) and trying running the test example:

   ::

       docker run hello-world

Windows 7 and Windows 8
~~~~~~~~~~~~~~~~~~~~~~~

Detailed installation instructions are available
`here <https://docs.docker.com/toolbox/toolbox_install_windows/>`_. For
our purposes, you can simply:

1. You're killing me, Smalls.

Mac OSX
~~~~~~~

Detailed installation instructions are available
`here <https://docs.docker.com/docker-for-mac/>`_. For our purposes,
you can simply:

1. `Download <https://download.docker.com/mac/stable/Docker.dmg>`_ the
   installer.

2. Double click on the installer and drag ``Docker.app`` into your
   Applications folder.

3. Double click on ``Docker.app`` to start Docker.

4. Open a shell (e.g. ``terminal.app``) and trying running the test
   example:

   ::

       docker run hello-world

Unix/Linux
~~~~~~~~~~

¯\\\_(ツ)_/¯

Install Anaconda
----------------

Anaconda is a software package for Python (and R and sometimes C...)
that handles the installation of common Python packages for you, making
it easier to create and manage portable environments. We'll be using it
inside of Docker to ensure that everyone is running under the same
environment. See `this page <https://www.continuum.io/blog/developer-blog/
anaconda-and-docker-better-together-reproducible-data-science>`_ 
for more on how Docker and Anaconda fit together.

1. Get the latest Anaconda for Python 3 image:

   ::

       docker pull continuumio/anaconda3

2. Test that your installation worked:

   ::

       docker run continuumio/anaconda3 /opt/conda/bin/conda info

Running Jupyter Notebooks
=========================

Jupyter notebooks are...

1. You can fire up a notebook using the following command:

   ::

       docker run -it -p 8888:8888 -v ~/repos/ihme-python-course/:/home/ihme-python-course/ continuumio/anaconda3 /opt/conda/bin/jupyter notebook --ip='*' --no-browser --notebook-dir=/home/ihme-python-course/

   What do all of these arguments mean?

   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Argument                     | Value                                                       | Description                                                                                                        |
   +==============================+=============================================================+====================================================================================================================+
   | ``-it``                      |                                                             | Run the Docker container interactively                                                                             |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``-p``                       | ``8888:8888``                                               | Map the 8888 port of the Docker container to the local port so that you can connect to it via your web browser     |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``-v``                       | ``~/repos/ihme-python-course/:/home/ihme-python-course/``   | Maps ``<host directory>:<container directory>`` so that the repo you've downloaded is visible to the container     |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``continuumio/anaconda3``    |                                                             | The name of the Docker container to be run                                                                         |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``/opt/conda/bin/jupyter``   |                                                             | The program to execute inside of the container (Jupyter)                                                           |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``notebook``                 |                                                             | This tells Jupyter to start a Notebook server                                                                      |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``--ip``                     | ``'*'``                                                     | Configures Jupyter to respond to any user that can connect to the container                                        |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``--no-browser``             |                                                             | Prevents Jupyter from trying to automatically launch a web browser, since the Docker container does not have one   |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | ``--notebook-dir``           | ``/home/ihme-python-course/``                               | Sets the root directory for the Jupyter server to the same one mapped under ``-v``                                 |
   +------------------------------+-------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

   If you've followed all of the directions above exactly, you shouldn't
   need to edit any of these right now. If you've saved into a
   non-standard location, you may need to change the first part of your
   ``-v`` argument.

   There are many more options you can specify. See the corresponding `Docker
   <https://docs.docker.com/engine/reference/commandline/run/>`_ and `Jupyter
   <https://jupyter.readthedocs.io/en/latest/running.html#introducing-
   the-notebook-server-s-command-line-options>`_ documentation.

2. Navigate to `localhost:8888 <http://localhost:8888>`_ in your web browser. 
   You should see a listing of the files and directories inside this repo.

3. Click on ``Lecture 1`` then ``Setting up Python.ipynb`` and a
   notebook should open.
