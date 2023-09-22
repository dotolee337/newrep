
def cutstr(st,wd,idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

import math
def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi /2)

def mt_elog():
    return math.log(math.e)

def mt_sxp(x):
    return math.exp(x)

def mt_pi():
    return math.pi

import random as rd

def rd_int(x,y) :
    return rd.randint(x,y)

def rd_list(this) :
    return rd.choice(this)

def rd_rd():
    return rd.random()

def rd_nmvar() :
    return rd.normalvariate(0,1)
