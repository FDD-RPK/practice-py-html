# 두 숫자를 저장한 변수를 만들고 합계를 출력하시오
a = 10
b = 25
result = 50
print(type(a+b))
print('합계', result)

# +연산자의 양쪽 중에 하나라도 문자열이면 나머지도 문자열로 바꿔서 연결한다 - JS
# python에서는 타입을 변환시켜줘야한다
# print('합계:' + result)    <-  오류

print('합계:' + str(result))

# f문자열을 사용할 수 있다
print(f'합계:{result}')

name = input('이름입력:')
print(type(name))