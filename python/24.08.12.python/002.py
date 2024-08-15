# 파이썬의 타입(자료형) - 언어가 처리 가능한 종류
# - oracle의 타입 : number, varchar2, date
# - js의 타입 : object(참조타입) vs 기본타입(string, number, boolean, undefined)
#               참조타입 : 값을 가리킨다
#               기본타입 : 값을 가진다

# 모든 타입은 객체로 표현
# python의 타입
# 기본타입 - 값을 하나 다룬다 : int, float, bool
# - sequence : str, list(일반 배열), tuple(읽기전용 배열) - index 사용가능
# - dictionary : JS의 객체
# - set : 집합인데 값이 중복될 수 없고 순서가 없다(인덱스 사용 불가)
# 특수타입 - None

lst = [1,2,3,1,2,3]
s  = set(lst)
print(s)

s2 = list(s)
print(s2)

print(lst[0])