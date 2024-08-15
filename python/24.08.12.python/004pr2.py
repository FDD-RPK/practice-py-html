# 문자열의 길이를 출력하라
# "pneumonoultramicroscopicsilicovolcanoconiosis"
print(len("pneumonoultramicroscopicsilicovolcanoconiosis"))



# 화면에 아래 문장을 출력하라.
# C:\Windows
print("C:\\Windows")

# 다음 코드를 실행해보고 \t와 \n의 역할을 설명하라
# print("안녕하세요. \n만나서\t반갑습니다.")
print("안녕하세요. \n만나서\t반갑습니다.")
print("\\n은 줄을 바꾸는 역할\n\\t는 공백을 주는 역할이다")
# \n -> 엔터  \t -> 스페이스바

# print 함수에 두 개의 단어를 입력한 예제이다. 아래 코드의 출력 결과를 예상하라
# print ("오늘은", "일요일")
print("오늘은", "일요일")
print("두 단어 사이에 공백(띄어쓰기)가 시행되었다")
print("오늘은")
print("일요일")
print("오늘은", end=' ')
print("일요일")

# 다음 코드의 실행 결과를 예측하라
# 실수 = 4.7
# print(int(실수))
실수 = 4.7
print(int(실수))
print("나머지는 사라지고 몫만 남는다")

# 변수에 바인딩된 실수를 반올림 후 정수로 출력하라
# 실수 = 4.7
# 4
실수 = 4.7
print(int(실수 + 0.5))

# 변수에 바인딩된 실수를 소수점 둘째 자리이하를 버림 후 출력하라
# 실수 = 4.71
print(int(실수*10)/10)