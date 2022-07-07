# Pysindy Validation

Repo that aims to validate the power and usefullness of PySindy library

## Getting started

We used the original PySindy repo published by Professor Steven Brunton team [link](https://github.com/dynamicslab/pysindy)

## Objective

The goal of use PySindy is to identify the process dynamics of a SISO (single input, single output) system, so that we can have a better understanding of the dynamics that govern the process. Althoug we usually model a flow loop as a FOPDT (first order plus dead time) model, we wanna use PySindy to further understand the full dynamic behavior of the system. 

We also have to remember that in real cases like this, the full dynamical system is governed by the process dynamics (air volumetric flow) + actuator dynamics (which is the control valve, typically a butterfly type of valve) + instrument dynamics (which is the flow sensor that uses differential pressure to measure flow) and finnally the closed loop PID controller dynamics.

Latter, we wanna try to use PySindy to model a MIMO (multiple input, multiple output) system, so that we can use a data-driven model identification approach and use the discovered model with a MPC controller.

## How to run the repo

Clone the repo and run the jupter notebook *pysindy_flowloop_example.ipynb*

The src folder contains all the necessary python code to run the example.

## Main referrences used to inspire us and also to guide us in order to use PySindy propperly.


1. [PySINDy: A Python package for the Sparse
Identification of Nonlinear Dynamics from Data](https://arxiv.org/pdf/2004.08424v1.pdf)
2. [Youtube channel with System Identification lectures from the Brazillian Professor Luis Aguirre](https://www.youtube.com/watch?v=TWdgSG0sMlQ&list=PLALrL4i0Pz6DrrCkkJ-k-_S3qi1bFzUUu)
3. [state space modeling example in python](http://apmonitor.com/pdc/index.php/Main/StateSpaceModel)
4. [Kalman filtering book](https://drive.google.com/file/d/0By_SW19c1BfhSVFzNHc0SjduNzg/view?usp=sharing&resourcekey=0-41olC9ht9xE3wQe2zHZ45A) e com esse [repo](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)
5. [Cool Pysindy example found in the internet](https://www.futurescienceleaders.com/blog/2022/06/discovering-the-governing-differential-equations-of-a-combustion-system-using-sindy/)
6. [Amazing example and code inspiration that used PySindy](https://github.com/bstollnitz/sindy)
