# 연산
# 덧셈
a = 3
b = '4'
print(3+4)
print(3+int(b))

# 예외 : 문법이 틀린 것이 아닌 실행 중 문제가 발생
# 파이썬은 예외 상황을 에러 클래스로 정의했다
# 자바스크립트의 경우 예외가 발생하면 try ~ catch ~
# try {
#   예외가 발생할 지 모르는 코드
# } catch(err) {
#   예외 처리하는 코드
# }

# 곱셈
print(3*4)
print('3'*40)

# 나눗셈, 몫, 나머지
print(15/4)     # 3.75
print(15//4)    # 3
print(15%4)     # 0.75
# JS에는 몫연산이 없다 -> 함수를 사용
# Math.floor(15/4)    ->     3

# 파이썬은 함수를 import한 다음 사용.
# 내장함수 : import없이 사용할 수 있는 기본 함수
# print(), type(), int(), float(), str(), set(), list(), tuple(), dict()

# len
print(len('hello'))
print(len([1,2,3,4,5]))

