import sys, getopt
import matplotlib.pyplot as plt
import random as rd
import scipy as sp
import numpy as np

nargin = len(sys.argv)

# Number of iterations the simulation will run for
n = 10000
# Rabbit growth rate
a = 0.5
# Rabbit death rate
b = 0.01
# Fox death rate
c = 0.5
# Fox reproduction rate
d = 0.01

# Time step of simulation
dt = 0.1
# Initial population of prey
x0 = 100
# Initial population of predators
y0 = 100

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:x:y:a:b:c:d:t:")
except getopt.GetoptError:
    print 'predprey.py -n <no. of iterations> -x <init. pop. prey> -y <init. pop. pred.> -a <prey growth rate> -b <prey death rate> -c <pred. death rate> -d <prey reproduction rate> -t <timestep>'
    sys.exit(2)

for opt, arg in opts:
    if opt == '-n':
        n = int(arg)
    elif opt == '-x':
        x0 = float(arg)
    elif opt == '-y':
        y0 = float(arg)
    elif opt == '-a':
        a = float(arg)
    elif opt == '-b':
        b = float(arg)
    elif opt == '-c':
        c = float(arg)
    elif opt == '-d':
        d = float(arg)
    elif opt == '-t':
        dt = float(arg)


def lv(n,x0,y0,a,b,c,d,dt):

    paramString = 'n: {} x0: {} y0: {} a: {} b: {} c: {} d: {} dt: {}'.format(n,x0,y0,a,b,c,d,dt)
    print paramString

    # Initialise array with first values at zeroth index
    x = np.zeros(n); x[0] = x0;
    y = np.zeros(n); y[0] = y0;

    # Calculate n iterations of the populations
    for i in xrange(1,n-1):
        # xc/yc are current x and y values
        xc = x[i-1]
        yc = y[i-1]
        # Set threshold below which a population is declared dead
        xc = 0 if xc < 0.1 else xc
        yc = 0 if yc < 0.1 else yc
        
        
        # Calculate the next step
        x[i] = xc + (xc*a - xc*b*yc) * dt
        y[i] = yc - (yc*c - yc*d*xc) * dt

        # Define timeline for plotting
        timeline = np.arange(0.,dt*n,dt)

    # Make plots
#    plt.figure()

#    plt.plot(x,y)
#    plt.ylabel('Prey')
#    plt.xlabel('Predators')
#    plt.title(paramString)

    plt.figure()
    plt.plot(timeline,x,label='Prey')
    plt.plot(timeline,y,label='Predators')
    plt.ylabel('Population')
    plt.xlabel('Time')
    plt.title(paramString)
    plt.legend()

lv(n,x0,y0,a,b,c,d,dt)

# Validate what happens if we decrease the prey reproduction rate q:
# Take the same parameters and make plots with decreased q - q is analogous to a in this case.
plt.show()

