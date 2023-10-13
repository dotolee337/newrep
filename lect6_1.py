"""
#1번
for i in range(1,6):
    for j in range(6-i):
        print("*",end=" ")
    print()
    
for i in range(5, 0, -1):
    print("*" * i)

#2번
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(1,6):
    print("*" * i)
"""
"""
#3번
for i in range(5):  
    for space in range(3-i):
        print("*",end=" ")
    print()                        #->고치기
    for star in range(i+1):
        print()

for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
"""
"""
#4번
for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
for i in range(6,0,-1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars)
"""
#5x5
#정상출력
"""
num = 0
list = [ ]
for i in range(5):
    for j in range(5):
        num += 1
        list.append(num)
    print(list)
    list = []
"""    
#세로출력
"""
for i in range(5):
    num = i+1
    list = [i+1]
    for j in range(4):
        num += 5
        list.append(num)
    print(list)       
    list = []

list = []
for i in range(1,6):
    for j in range(1,6):
        num = ((j - 1)* 5) + i
        list.append(num)
    print(list)
    list = []
"""
"""
#역순
num = 26
list = [ ]
for i in range(5):
    for j in range(5):
        num -= 1
        list.append(num)
    print(list)
    list = [ ]
"""
#가위바위보
"""
import random

def get_computer_choice():
    choices = ['1','2','3']
    return random.choice(choices) 

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice,pcnum)
        
    if user_choice == pcnum :
       print("무승부")
       return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return
         
print("1: 가위")
print("2: 바위")
print("3: 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
#pcnum = get_computer_choice()

determine_winner(chnum)
"""
#파일 생성
#f = open("new.txt",'w')

f = open("temp.txt",'w')
f.close()

#파일쓰기

file = open("text")