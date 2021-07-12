# Projects: Digital Signal Processing

This repository contains various projects made with Python / Jupyter Notebooks in order to solve a series of exercises about the basics of Digital Signal Processing.

## How to run:

### Docker:
The best way to run these exercises is to directly download the image from DockerHub:

https://hub.docker.com/r/reborafs/dsp-untref

How to run the image on Ubuntu: 

```sudo docker run -p 8888:8888 reborafs/dsp-untref:main```

The -p tag here is important—you will need to connect the port that the notebook is running on inside the container with your local machine.

### Direct Download:
If you choose to directly download the .zip file from github you can use the requirements .txt to install or verify all the libraries used in this project. 
Basically, you should have installed Numpy, Scipy, Matplotlib and Librosa.
