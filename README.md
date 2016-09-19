Intro
=====
Lorem ipsum

Getting started
===============
In order to make sure everyone is operating off of the same page, we're going
to be using [Docker](https://www.docker.com/what-docker) and 
[Anaconda](https://www.continuum.io/anaconda-overview) to setup consistent
Python development environments.

Please follow the installation instructions below to make sure you have a 
working Python environment prior to the beginning of the course.

Install Docker
--------------
Docker enables you to create "containers" which provide consistent environments
in which to run your code. This way, you can run the software you write on 
different machines (e.g. your laptop vs the computing cluster) without 
having to spend too much time worrying about adapting it.

We're going to just be using some very basic features of Docker, so if you'd
like to learn more refer to 
[this page](https://docs.docker.com/engine/understanding-docker/).

### Windows
Detailed installation instructions are available
[here](https://docs.docker.com/docker-for-windows/). For our purposes, you can
simply:

1. [Download](https://download.docker.com/win/stable/InstallDocker.msi) the
installer.

2. Double click on the installer and follow the prompts (keeping all options 
as defaults is fine).

3. Open a shell (e.g. `cmd.exe`) and trying running the test example
`docker run hello-world`.

### Mac OSX
Detailed installation instructions are available
[here](https://docs.docker.com/docker-for-mac/). For our purposes, you can
simply:

1. [Download](https://download.docker.com/mac/stable/Docker.dmg) the installer.

2. Double click on the installer and drag `Docker.app` into your Applications
folder.

3. Double click on `Docker.app` to start Docker.

4. Open a shell (e.g. `terminal.app`) and trying running the test example
`docker run hello-world`.

### Unix/Linux
Lorem ipsum

Install Anaconda
----------------
Anaconda is a software package for Python (and R and sometimes C...) that
handles the installation of common Python packages for you, making it easier
to create and manage portable environments. We'll be using it inside of Docker
to ensure that everyone is running under the same environment. See 
[this page](https://www.continuum.io/blog/developer-blog/anaconda-and-docker-better-together-reproducible-data-science) for more on how
Docker and Anaconda fit together.

1. Get the latest Anaconda for Python 3 image:
    ```
    docker pull continuumio/anaconda3
    ```

2. Run a Jupyter Notebook Server from inside the Anaconda Docker image:
    ```
    docker run -i -t -p 8888:8888 continuumio/anaconda3 /opt/conda/bin/jupyter notebook --ip='*' --no-browser
    ```
