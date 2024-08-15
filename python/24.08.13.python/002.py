# 시퀀스 타입 : 자바나 자바스크립트는 iterable하다 - str, list, tuple
# 리스트와 튜플의 차이 : 읽기전용-튜플, 편집가능-리스트
# 리스트와 str의 차이 : string[0]='A'라는 연산 불가

# tuple
# a = (3,4)
# b = 3,4

# 원소 1개짜리 튜플을 만들때
# c = 3,      # ,를 찍지 않으면 튜플이 아닌 실수로 판단

# 튜플을 이용해 한번에 여러개의 변수를 생성
# a, b = 3, 4

# JS에서 irumm과 nai로 구성된 객체 ob가 있다. 객체의 속성을 irum, nai에 풀어헤쳐 대입한다
#       const irum = ob.irum;
#       const nai = ob.nai;
#       const {irum, nai} = ob;         - 구조분해할당

# 두 변수의 값을 바꾼다
x, y = 10, 20
x, y = y, x         #python style 방법
print(x, y)

tmp = y
y = x
x = tmp             #범용성(미는퍼즐 맞추기 느낌)

# set : 중복되지 않는다. 순서가 없다 -> 리스트의 중복 제거

my_list = [1,3,5,7,7,10]
my_tuple = tuple(my_list)

my_list2 = list(my_tuple)

my_set = set(my_list)
my_list3 = list(my_set)
print(my_list3)


# tmp에 20 대입
# y에 10 대입
# x에 20 대입       =   y=10    x=20    tmp=20


# set : 중복되지 않는다. 순서가 없다 -> 리스트의 중복 제거