# Simple CA simulator in Python
#
# *** Game of Life Rule ***
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP

RD.seed(42)

width = 50
height = 50
initProb = 0.2
useInit = 0;
useStep = 2;
t = 0;

def init():
    if useInit:
        init1();
    else:
        init2();
        
def init1():
    global time, config, nextConfig

    time = 0
    
    config = SP.zeros([height, width])
    for x in xrange(width):
        for y in xrange(height):
            if RD.random() < initProb:
                state = 1
            else:
                state = 0
            config[y, x] = state

    nextConfig = SP.zeros([height, width])

def init2():
    global time, config, nextConfig

    time = 0

    config = SP.zeros([height, width])
    nextConfig = SP.zeros([height, width]);
    one = (5,5);
    two = (5,25);
    three = (5,35);
    
    config[one[0]][one[1]+1] = 1;
    config[one[0]][one[1]+2] = 1;
    config[one[0]+1][one[1]] = 1;
    config[one[0]+1][one[1]+3] = 1;
    config[one[0]+2][one[1]+1] = 1;
    config[one[0]+2][one[1]+2] = 1;

    config[two[0]][two[1]] = 1;
    config[two[0]][two[1]+1] = 1;
    config[two[0]+1][two[1]] = 1;
    config[two[0]+1][two[1]+1] = 1;
    config[two[0]+2][two[1]+2] = 1;
    config[two[0]+2][two[1]+3] = 1;
    config[two[0]+3][two[1]+2] = 1;
    config[two[0]+3][two[1]+3] = 1;

    config[three[0]][three[1]+1] = 1;
    config[three[0]+1][three[1]+2] = 1;
    config[three[0]+2][three[1]] = 1;
    config[three[0]+2][three[1]+1] = 1;
    config[three[0]+2][three[1]+2] = 1;
    
def draw():
    PL.cla()
    PL.pcolor(config, vmin = 0, vmax = 1, cmap = PL.cm.binary)
    PL.axis('image')
    PL.title('t = ' + str(time))

def step():
    if useStep == 0:
        step0();
    elif useStep == 1:
        step1();
    else:
        step2();
        
def step0():
    global time, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y, x]
            numberOfAlive = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    numberOfAlive += config[(y+dy)%height, (x+dx)%width]
            if state == 0 and numberOfAlive == 3:
                state = 1
            elif state == 1 and (numberOfAlive < 3 or numberOfAlive > 4):
                state = 0
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

def step2():
    global time, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y, x]
            numberOfAlive = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    numberOfAlive += config[(y+dy)%height, (x+dx)%width]

            rd = RD.random();
            if state == 1:
                if numberOfAlive < 3:
                    if rd < 1-t:
                        state = 0
                elif numberOfAlive == 3 or numberOfAlive == 4:
                    if rd > 1-t:
                        state = 0
                else:
                    if rd < 1-t:
                        state = 0
            else:
                if numberOfAlive == 4:
                    if rd < 1-t:
                        state = 1                        
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config
    

    
def step1():
    global time, config, nextConfig

    time += 1

    for x in xrange(width):
        for y in xrange(height):
            state = config[y, x]
            numberOfAlive = 0
            for dx in xrange(-1, 2):
                for dy in xrange(-1, 2):
                    numberOfAlive += config[(y+dy)%height, (x+dx)%width]
            if state == 0 and numberOfAlive == 7:
                state = 1
            elif state == 1 and (numberOfAlive != 2 and numberOfAlive != 7):
                state = 0
            nextConfig[y, x] = state

    config, nextConfig = nextConfig, config

    
import pycxsimulator
pycxsimulator.GUI().start(func=[init,draw,step])
