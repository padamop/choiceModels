# NumPy is an extension to the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large library of high-level mathematical functions to operate on these arrays
import numpy as np
# matplotlib is a plotting library for the Python programming language 
import matplotlib.pyplot as plt

# We create a method to plot two sets of values on a histogram     
def plotHistogram(data1, data2, label1='', label2='', title='', xlabel='', ylabel=''): # title, xlabel, and ylabel are optional parameters with default values set to ''
    plt.hist(data1, label=label1) # plot a histogram
    plt.hist(data2, color='r', alpha=0.5, label=label2) # plot another histogram 
    plt.xlabel(xlabel) # set the x axis label 
    plt.ylabel(ylabel) # set the y axis label 
    plt.title(title) # set the title of the plot
    plt.grid(True) # turn the axes grids on or off
    plt.legend() # place a legend on the current axes
    plt.show() # display a figure