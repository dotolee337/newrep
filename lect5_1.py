"""
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

#sys : Python 인터프리터와 상호작용하기 위한 함수를 제공
import sys

print(sys.version)
print(sys.argv)
"""

#stack 
list = []

#stack 값 넣기
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

#스택 상태 확인
print(list)

#스택에서 값 빼기
top = list.pop()
print(top) #3
print(list)
print(len(list))

#큐(Queue) 선입선출(First In First Out)
#빈 큐 생성
queue = []

#큐 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue)

#큐에서 값 뺴기
front = queue.pop(0)
print(front)
print(queue)
print(len(queue))