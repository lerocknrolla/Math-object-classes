# Math-object-classes

The *Frac* class and the *Morse player* set of functions were small Python class exercises to which I added various new functionalities:
- to *Frac*, I added interaction with floats and integers, and further tweaks are planned, but mostly I wanted to explore the interning mechanic;
- to the *Morse player*, which was originally a binary tree exercise, I wanted to add audio playback.

The rest of the classes are works in progress:
- *DirGraph* is a class of directed graphs; I like the representation using GraphViz, but I intend to add mathematical functionality that will allow a user to solve optimization and other such problems;
- *Base-n* is a simple number object for integers (and possibly other numbers, in the future) represented in a non-decimal base, printed out in a format that was convenient for a previous project;
- *Matrix* has only just been started, but I will be trying to implement it both using a list of lists as well as with a dictionary storing only non-zero values, according to the sparse matrix idea, and will also be adding functionality to operate with matrices as well as analyze them for invertibility, etc.

The ultimate goal is to integrate all these objects together, for example to calculate the adjacency matrix of a given directed graph.

All these projects are being worked on as Jupyter notebooks for presentation, since that will allow me to more easily demonstrate functionalities in the future.
