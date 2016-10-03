# Exercise 1

## Installing Anaconda

See [the README](../README.rst) for instructions on how to install Anaconda
on your system.


## Clone this repo
See [the README](../README.rst) again for instructions on cloning this repo
(into its recommended location of `~/repos/`).


## Opening the `python` interpreter

- Open up your terminal and type `python` at the command line
- Try typing some things in to see how they work... some suggestions:
    * `1 + 1`
    * `1.0 + 1`
    * `"hello world"`
    * `print("hello world")`
- Type `exit()` to exit


## Running `ipython`

- Open up the interactive IPython interpreter
    * `ipython`
- Try some of the same inputs as above
- Type `print?` and hit `return`
- Type `print(` and hit `tab`
- Type `exit()` to exit


## Exploring `jupyter notebook`

- Open up a terminal and navigate to the root directory of this repo (e.g. 
    `~/repos/ihme-python-course`)
- Type `jupyter notebook` to startup a notebook server
- Your web browser will most likely automatically open 
    * If not, you can navigate to 
        [http://localhost:8888/](http://localhost:8888/)
    * _Note_: if you're already running something on port `8888` it might start
        the server on a different port. Look for a message in your terminal 
        like
            The Jupyter Notebook is running at: http://localhost:8889/
        to find it.
- Use the file tree to navigate to the `Lecture 1/Exercise 1` directory and 
    and then click on `test-notebook.ipynb` to open it
- Follow the instructions in the notebook


## Run a script from the command line

- Examine [Exercise 1/test-script.py](Exercise 1/test-script.py) with your
    favorite editor or Spyder
- Run it from the command line
    * _Hint_: remember `python my-script.py`
- Change the message from "hello world" to something else and execute it


## _Optional_: Install `RISE`

- [`RISE`](https://github.com/damianavila/RISE) will add a new button to your
    Jupyter toolbar that'll allow you to view these notebooks in slideshow mode
- Click the new bargraph-esque icon in the toolbar to start a slideshow
- Use `spacebar` and `shift+spacebar` to navigate through the slides
- To edit how the slideshow is structured, take a look at 
    `View > Cell Toolbar > Slideshow`
