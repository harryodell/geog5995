# Geog5995 - Final assignment for PfSS course

This repository contains code pertaining to a simple agent based model (ABM) that simulates a scenario in which drunks must find their way home from the pub. Drunks are introduced to a limited virtual environment in which they move pseudo-randomly. The simulation runs until all drunks have made their way home.

## Motivation

The motivation behind this project was to fulfil the requirements for the final assignment of the [GEOG5995 Programming for Social Scientists: Core Skills [Python] course](http://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/ "GEOG5995") at Leeds University. The requirements of the project were given as:

* Pull in the data file and find out the pub point and the home points.
* Draw the pub and homes on the screen.
* Model the drunks leaving the pub and reaching their homes, and store how many drunks pass through each point on the map.
* Draw the density of drunks passing through each point on a map.
* Save the density map to a file as text.


## ABM

### Running the model

The model runs from the command-line or terminal. The user should download or clone the repository and navigate (in the prompt) to the local directory. Then, the model runs as:

```python drunks_ani.py [arg1]```

where  ```arg1``` is the max number of iterations.

When the model is running, two plots will appear. First is a plot of the initial environemnt and the next is an animation of the model. We use ```matplotlib.animation.FuncAnimation()``` to make the animation - this function provides a plot of the current state of the model following each iteration and is recommended because of its use in helping the user understand the interactions within the model.


### Model outputs

When the model stops running, it can be assumed that all the drunks have found their way home, or that the maximum number of iterations has been reached. 

A file will then be written out to the same directory in which the code is in:

* ```out.txt```: a text file providing a copy of the density of the final environment, denoting the amount of drunks that passed each point


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgemnts

Many thanks to Dr. Andy Evans for providing the material for the course and to his co-lecturers and teaching assistants for the delivery of the course. 
