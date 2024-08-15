# my_variable 이름의 비어있는 튜플을 만들어라
my_variable = ()
print(type(my_variable))

# 2016년 11월 영화 예매 순위 기준 top3를 movei_rank 이름의 튜플에 저장하라(순위 정보는 저장 X)
# 1. 닥터 스트레인지
# 2. 스플릿
# 3. 럭키
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(type(movie_rank))

# 숫자 1이 저장된 튜플을 생성하라
number1 = (1,)
print(type(number1))

# 다음 코드를 실행해 보고 오류가 발생하는 원인을 설명하라
    # t = (1, 2, 3)
    # t[0] = 'a'
    # Traceback (most recent call last):
    # File "<pyshell#46>", line 1, in <module>
    # t[0] = 'a'
    # TypeError: 'tuple' object does not support item assignment
# 튜플은 element값을 변경 불가

# t에는 1,2,3,4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1,2,3,4
print(type(t))
# 튜플

# 변수 t가 ('A','b','c')튜플을 가리키도록 수정 하라
t2 = ('a', 'b', 'c')
# 튜플은 변경 불가
t3 = ('A', 'b', 'c')

# 다음 리스트를 튜플로 변경하라
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest2 = ('삼성전자', 'LG전자', 'SK Hynix')
print(type(interest2))