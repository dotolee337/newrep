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

from datetime import datetime as dt

def get_dtnow():
    return dt.now()

def cvt_time2str(objtime) :
    return dt.strptime(objtime,"%Y-%m-%d")

def cvt_str2time(strftime) :
    obj = dt.now()
    return obj.strftime("%Y-%m-%d")

import os
def get_curdir():
    return os.getcwd()

def os_mkdir(pname) :
    return os.mkdir(pname) 

