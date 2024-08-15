# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 슬라이싱을 사용해서 홀수만 출력하라
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

# 슬라이싱을 사용해서 짝수만 출력하라
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라
nums2 = [1, 2, 3, 4, 5]
print(nums2[::-1])

# interest 리스트에 바인딩되어있는 데이터를 아래와같이 출력하라
# 삼성전자 Naver
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# interest2 리스트에 바인딩되어있는 데이터를 아래와같이 출력하라
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
interest2 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest2[0], end=' ')
print(interest2[1], end=' ')
print(interest2[2], end=' ')
print(interest2[3], end=' ')
print(interest2[4])

print((' ').join(interest2))

# # interest3 리스트에 바인딩되어있는 데이터를 아래와같이 출력하라
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest3 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest3[0], end='/')
print(interest3[1], end='/')
print(interest3[2], end='/')
print(interest3[3], end='/')
print(interest3[4])

# # interest4 리스트에 바인딩되어있는 데이터를 아래와같이 출력하라
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
interest4 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest4[0])
print(interest4[1])
print(interest4[2])
print(interest4[3])
print(interest4[4])

# 회사 이름이 슬래시('/')로 구분되어 하나의 문자열로 저장되어 있다
# 이를 interest5 이름의 리스트로 분리 저장하라
string = '삼성전자/LG전자/Naver'
interest5 = []
interest5.append(string[0:4])
interest5.append(string[5:9])
interest5.append(string[10:15])
print(interest5)

# 회사 이름이 슬래시('/')로 구분되어 하나의 문자열로 저장되어 있다
# 이를 interest6 이름의 리스트로 분리 저장하라
string2 = '삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우'
interest6 = []
interest6.append(string2[0:4])
interest6.append(string2[5:9])
interest6.append(string2[10:15])
interest6.append(string2[16:22])
interest6.append(string2[23:29])
print(interest6)