"""
my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print(my_set)
print(setItem)
"""
"""
my_set = {5, 8, 3, 7, 1, "h"}
print(my_set)
print(*my_set)

set_tmp = set("hello")
print(set_tmp)

set_item = {7, 8, 4, 2, "h"}
print(my_set | set_item)   #합집합
print(my_set.union(set_item))

print(my_set - set_item)   #차집합
print(my_set.difference(set_item))

print(my_set & set_item)   #교집합
print(my_set.intersection(set_item))

print(my_set)
my_set.add(9)   #추가
print(my_set)

my_set = {5, 8, 3, 7, 1, "h"}
#my_set.clear()
my_set.remove(5)    #요소 없으면 error
print(my_set)
my_set.discard(2)   #요소 없으면 넘어감
print(my_set)
"""
"""
my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"}
my_set.difference_update(set_item)  #공통요소 삭제
print(my_set)
"""
#변환 처리
"""
my_int = 10
my_str = str(my_int)
print(my_int,my_str)

print(my_int + 10)
my_str = str(my_int)
print(my_str)
#print(my_str + 10)
print(my_str + "hello")

my_str = '10'
my_int = int(my_str)
print(my_str,my_int)
print(my_int + 10)
#my_int2 = int("ten")
#print(my_int2)
"""
#연산
#a = 10
#b = 3
#c = a + b   
#c = a - b    
#c = a * b   
#c = a / b 
#c = a % b    
#c = a // b   
#c = a ** b  
#print(c) 

#할당 연산자
"""
a = 0
print(a)
a += 2
print(a)
a -= 1
print(a)
a *= 4
print(a)
a /= 2
print(a)
a **= 3
print(a)
"""
#비교 관계 연산자(boolean)

#a = 10
#b = 4
#c = a > b   
#c = a < b    
#c = a >= b   
#c = a <= b   
#c = a == b   
#c = a != b  
#print(c)
"""
#논리 연산자
a = 1
b = 0
print(a and b)  #둘다 1이여야 1이나옴(2진법) 
                #ex) 1010(10) and 0010(2) -> 0010(2)
print(a or b)   #둘중에 하나만 1이여도 1나옴(2진법)
                #ex) 1010(10) or 0010(2) -> 1010(10)
print(not a)    #반대 비트로 나옴 ex)1010(10) -> 0101(5)
print(not b)    

x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
print(not y)  
"""
#비트 연산자(모르면 계산기로 하기) 
#int 기본 32비트
a = 10
b = 3

print(a & b)   
print(a | b)   
print(a ^ b)    #xor 달린거 따라 순차적으로 계산 (not -> and 연산)
print(~a)       #앞의 부호비트도 같이 바뀌어서 음수가됨(부호비트: 0 = + / 1 = -)
print(a << 2)   #"<"의 개수와 방향만큼 이동

#멤버 연산자
my_list = [9, 4, 3, 7, 8, 'hi']
print(4 in my_list)
print(2 in my_list)

print(2 not in my_list)
my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_list)