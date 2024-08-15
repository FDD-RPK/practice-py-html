# 인덱싱
a = 'hello python'

print(a[0])         #h
print(a[1])         #e
print(a[5])

# 함수는 실행이 끝나면 값
print(a[11])        #n
print(a[-1])        #n
print(a[len(a)-1])  #n

# 문자열 슬라이싱
# JS : a.substr(0, 5)
#      a.substring(0, 5)
print(a[0:5])
print(a[:])
print(a[::2])


year = "2024/08/12"
# 08월
print(year[5:7]+'월')