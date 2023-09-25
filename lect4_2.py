#콜백 함수
"""
def prt_func(n) :      
    print("hello",n)

def callfunc(fx) :
        for i in range(5):  
            fx(i)

callfunc(prt_func)

#타입 힌트 - 콜백함수
def add(a, b) :
	return a + b

def add(a : int, b : int) -> int :
	return a + b

def greeting(in_name):
    gt_msg = None
    gt_msg = update_msg(name)
    return gt_msg 
"""
"""
#타입힌트 사용

def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg 

res = greeting("python")

for message in res:
    print(message)
"""
"""
#재귀함수
def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1)
"""
"""
#factorial
def ploop(n):
    if n == 0:
        print("end")
        return 1
    else:
        print(n,n-1,"=",n + n-1)
        return n * ploop(n-1)

print(ploop(5))
"""
"""
#피보나치 수열
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci(n-1) + fibonacci(n-2)
       
res = fibonacci(4)
print("res = ",res)        
"""
#==================
"""
#사용 가능 메소드
import calc

print(dir(calc))

#calc 모듈 호출
add_res = calc.add(4,2)
sub_res = calc.sub(4,2)
mul_res = calc.mul(4,2)
div_res = calc.div(4,2)
#or
print(calc.add(4,2))
print(calc.sub(4,2))
print(calc.mul(4,2))
print(calc.div(4,2))

#alias 사용
import calc as cl

# 수정확인
add_res = cl.add(4,2)
add_res = cl.sub(4,2)
add_res = cl.mul(4,2)
add_res = cl.div(4,2)
"""
"""
#circle mod

import mod.circle_mod as cm

print(cm.pi)
print(cm.cc_area(4))
print(cm.cc_len(5))

#문자열 자르기

def cutstr(st,wd,idx) :
    tmp = st.split(wd)
    res = tmp[idx]
    return res

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)
print(r5)

#문자유틸 모듈화
import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)
"""
#내장모듈
#import math
"""
import math
sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi /2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi
print(pi_res)

fc_res = math.factorial(4)
print(fc_res)

import mod.str_util as mu
res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog()
print(el)
"""
#import random
"""
import random as rd

res = rd.randint(1,100)
print(res)

my_list = ["apple","banana","cherry"]
lres = rd.choice(my_list)
print(lres)
#0.0~1.0 까지 랜덤
fres = rd.random()
print(fres)
#정규분포
nvres = rd.normalvariate()
print(nvres)
"""
"""
#모듈화
import mod.utils as mu
my_list = ['apple','banana','cherry']
print(mu.rd_int(1,100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar())

#from datetime 
from datetime import datetime as dt
#현재 시간 출력 
print(dt.now())
#특정 시간대의 현재 시간 출력
from pytz import all_timezones
tz = timezone('UTC')
print("timezone : ",dt.now(tz))

#문자열을 날짜로 변환
dat_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string)
"""
"""
from datetime import datetime as dt
import mod.str_util as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res)
"""
"""
#import os #운영체제 상호작용 함수 제공
import os

#현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경
os.chdir('../')

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력
print(os.listdir())

#디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir)

#디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())
"""
#os 모듈 확인 
import os
import mod.utils as mu

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())
#import sys

#print()
#import os #인터프리터와 상호작용
