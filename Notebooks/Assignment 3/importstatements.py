# Basic imports that are required for the smooth use of Python
import numpy as np                # Absolutely necessary
from scipy import signal          # For signal processing tools
from scipy import fftpack as fft  # Fourier transform and spectral analysis
import math as math               # Not always required. But can simplify the matrix/linear algebraical calculations 
import matplotlib.pyplot as plt

#import itertools                  # used to iterate over all combinations of parameters for a certain plot
# alternative: plotly - also for jupyterLab

## WAV files
from scipy.io import wavfile
import warnings                   # used to ignore some warnings in WAV-file reading
warnings.simplefilter(action='ignore', category=wavfile.WavFileWarning)

## Loading Matlab files
from scipy.io import loadmat  # To load a matlab data file.

## Breakpoints (if needed) for debugging
import pdb     # Setting breakpoints for debugging

## HTML/CSS styling
from IPython.display import HTML
def css_styling():
    return HTML(open("../assets/styles/custom.css",'r').read())


## Plot parameters
#plt.ioff()                        # interactive mode off -- this means you need plt.show() to show the plots
#plt.rcParams['figure.figsize'] = [12, 8]
#plt.rcParams.update({'font.size': 22})

# Define the Pole-Zero plot function here.

def PoleZeroPlot(B,A=(1,)):
    zeroes = np.roots(np.array(B))
    poles = np.roots(np.array(A))

    #print('The zeroes of H(z) are: '+'\t'.join(['{:3.3f}'.format(x) for x in zeroes]))
    #print('The poles of H(z) are: '+'\t'.join(['{:3.3f}'.format(x) for x in poles]))
    print('Poles are plotted using ''x'' and zeros as filled in circles ''o''.') 
    fig = plt.figure(); fig.clf()
    ax = fig.add_subplot(111)
    ax.plot(np.real(zeroes),np.imag(zeroes),'o',color='b',markersize=8)
    ax.plot(np.real(poles),np.imag(poles),'x',color='r',markersize=8)
    ax.set_xlim((-1.5,1.5))
    ax.set_ylim((-1.5,1.5))
    # Plot the unit circle
    ax.plot(np.cos(np.arange(0,2*np.pi,np.pi/100)),np.sin(np.arange(0,2*np.pi,np.pi/100)),\
            color='k')
    ax.set_aspect('equal')
    #plt.axes().set_aspect('equal')
    ax.grid('on')
    #fig.show()
    
def splot(X, Y, title = '', lb = None, axis = ['', ''], sname = '', tsp = True):
    '''
    Simple Plot Function
    
    X : List of arrays containing plotting data on x-axis
    Y : Corresponding y values
    aadede
    title      : title of plot
    axis       : list with two elements containing name of x- and y axis 
    sname      : name of saved plot file
    tsp        : transparent background (default : True)
    '''
    
    ## make a figure with axes
    fig, ax = plt.subplots(1, figsize=(7, 3.5))
    
    #make axis values biggel
    ax.tick_params(axis='both', which='major', labelsize=12)

    ## make plot title
    ax.set_title(title, size = 16)
    
    ## lable axis
    plt.xlabel(axis[0], size = 14)
    plt.ylabel(axis[1], size = 14)
    
    ## plot the data
    labl = False if lb == None else True
    if type(X) == list and len(X) > 1:
        if lb == None:
            lb = ['']*len(X)
        for i in range(len(X)):
            ax.plot(X[i], Y[i], lw = 2, label = lb[i])
    else:
        ax.plot(X, Y, lw = 2, label = lb)
    
    if labl == True:
        plt.legend()
    plt.grid()
    plt.tight_layout()
    
    if sname != '':
        plt.savefig(sname, transparent = tsp, dpi = 300)
    plt.show()