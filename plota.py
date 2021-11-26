'''
============================================================================
This program takes in the file path to a document containing two dimensional
data whose delimiter is ','.
it then prints the correlation between the data
and plots the scatter plot of your data 
============================================================================
'''

#importing the necessary libraries
from matplotlib import pyplot as plt
import numpy as np

#loads the document as a numpy array, unpack it into variables x and y respectively
#return an array of x and y respectively
def readcsv(csvfile):
    x,y = np.loadtxt(csvfile, unpack=True, delimiter=",")
    return x,y

#calls the readcsv function and assigns its output to variables x and y
def plotcsv(csvfile):
    x,y = readcsv(csvfile)
    corr = np.correlate(x,y)#finds the correlation between x and y

    print('The correlation between x and y is:', corr)
    
    plt.scatter(x,y) #plots the scatter plot of x and y
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()


'''
============================================================================
To use this module, first move it to your site-packages folder
Next, import all its functionalities

e.g. 
from plota import *

Then, call the plotcsv function and pass into it a valid file path to a document
containing two dimensional data separated by a comma

e.g.
plotcsv(ex_file.txt')
==============================================================================
'''
