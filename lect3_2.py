"""
#식별 연산
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)  
print(x is z)  
print(x is not y)  

#식별
a = 5
b = 5
print(a is b)
print(a is not b)

print(3 == 3.0)
print(3 is 3.0)

#특성
a = [3 , 5, 1]
b = a
print(a is b)

a[0] = 2     #
print(a,b)
print(a is b)
"""
#연산자 결합 순서
#x = 2 ** 3 ** 2
#print(x)    

#a = 2 + 3 * 4 
#a = 10 / 5 / 2
#a = 2 ** 3 ** 2
#a = 2 ** (3 ** 2)
#a = 10 % 3 % 2
#a = 1 + 2 > 3 
#a = 4 - 1 < 2
#a = not False and True
#a = not True or False and True
#a = 1 & 2 | 3 ^ 4
#a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
#a = 2 * -3 // 2
#a = 1 == 2 != 3        
#print(a)
"""
#조건문
x = 10

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is zero")
    
#if 짝수 홀수
num = 23
if num%2 == 0:
    print("짝수")
else:
    print("홀수")

#if a == b 
a = 5
b = 7
if a == b:
    print("a는 b와 같다")
else:
    print("a는 b와 다르다")

#if 두수 비교 
a = 45
b = 53
char = a
if char == "a" or char == "b"
    print("'a' 또는 'b'입니다")
else:
    print("a도 b도 아닙니다")
"""
"""
#반복문
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#이중 for문
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)

# for 0 ~ 9 출력
for i in range(10):
    print(i)
#문자열 한글자씩 출력    
for char in "Python":
    print(char)
#리스트 요소 반대로 출력 (reversed)  
for fruit in reversed(fruits):
    print(fruit)
#리스트 요소 반대로 출력 (sorted)
for fruit in sorted(fruits,reverse = True):
    print(fruit)

#구구단 출력( 이중 for문)
for i in range(1,10):
    for j in range(1,10):
        print(i,"x",j,"=",i*j)
"""
"""
#for ~ else 문
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
 #반복분 제어
for i in range(10):
    if i == 7:
        break
    elif i == 1:
        continue
    else:
        pass

    print(i)
# while 문
i = 1

while i <= 5:
    print(i)
    i += 1

#while 0~9까지 출력
i = 1
while i <= 9:
    print(i)
    i += 1

#while 한글자씩 출력
i = 0
char = "python"
while i < len(char):
    print(char[i])
    i += 1
"""
#1부터 10까지 총합 출력
i = 0
sum = 0
while i < 11:
    sum = sum + i
    i += 1
print(sum)

#1~ 100 까지 짝수 홀수 출력

while i <= 100:
    if i%2 == 0:
        print("짝수:", i)
    else:
        print("홀수:", i)
    i += 1
    
# 1~100 까지 7의 배수
i = 1
while i <= 100:
    if i%7 == 0:
        print("7의 배수:",i)
    else:
       pass
    i += 1

    
    