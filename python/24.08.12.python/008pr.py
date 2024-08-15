# 변수 one과 two에는 각각 문자열이 바인딩 되어있다
# 두 변수와 문자영ㄹ 이어 붙이기를 이용하여 'hello! python'과 같이 출력하라
one = "hello"
two = "python"
print(one+'! '+two)

# 변수에 문자열이 바인딩 되어 있다
# 변수와 문자열의 더하기 및 곱하기를 응용하여 다음과 같이 출력하라
# python java python java python java python java
one = 'python'
two = 'java'
print((one+' '+two)*4)

# lang이 바인딩하는 문자열에서 첫 번째와 세 번째 문자를 출력하라
lang = 'python'
print(lang[0], lang[2])

# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라
# license_plate = "24가 2210"
license_plate = "24가 2210"
print(license_plate[4:8])
print(license_plate[-4:])

# 인덱싱을 사용해서'홀'만 출력하라
string = "홀짝홀짝홀짝홀짝"
print(string[::2])

# 문자열을 거꾸로 뒤집어 출력하라
string = "PYTHON"
print(string[::-1])

# 다음의 전화번호에서 하이푼('-')을 제거하고 다음과 같이 출력하라
phone_number = "010-1111-2222"
lst = phone_number.split("-")
print(lst[0], lst[1],lst[2])
print(phone_number.replace('-',' '))

# 010 1111 2222
print(phone_number[0:3], phone_number[4:8], phone_number[9:13])

# 다음의 전화번호에서 하이푼('-')을 제거한 숫자를 모두 붙여 출력하라
print(phone_number[0:3]+phone_number[4:8]+phone_number[9:13])

# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경 후 출력하라
string = 'abcd'
print(string.capitalize())    # 첫글자를 대문자롤 바꾸는 함수
string = 'A' + string[1:]
print(string)

# 문자열에서 각 단어를 한 라인에 하나씩 출력하라
string = "국어 영어 수학 과학 경제 지리 물리 화학 생물"
print(string[0:2])
print(string[3:5])
print(string[6:8])
print(string[9:11])
print(string[12:14])
print(string[15:17])
print(string[18:20])
print(string[21:23])
print(string[24:26])

lst = string.split(' ')
for element in lst :
    print(element)