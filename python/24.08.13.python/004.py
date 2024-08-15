# dictionary

# JS에서는
# const obj = {irum:'홍길동', nai:20}

# class = 객체의 설계도

obj = {'irum':'홍길동', 'nai': 20}    # dictionary-python

# class Saram {
#     String name;
#     int nai;
#     public Saram(String name, int nai) {
#         this.name = name;
#         this.nai = nai;
#     }
# }
# Saram saram = new Saram("홍길동", 20);     #  java


# 딕셔너리는 자바스크립트의 객체에 해당
# 딕셔너리는 키와 값의 형식으로 데이터를 저장
# JS 객체 : const obj = {nickname:"spring"}
# 데이터를 구성하는 형태 = {키:'값'}
# 키를 지정해서 값을 읽어낸다
my_d = {'irum':'spring', 'nai':20}
a = 'irum'

# 키를 직접 적을 수도 있고 변수로 대신할 수도 있다
print(my_d['irum'])
print(my_d[a])

# 키가 없다면? KeyError
# print(my_d['name'])

# 키와 값의 쌍인 아이템을 추가
my_d['e-mail'] = 'hello@naver.com'
print(my_d)

# 변경하기
my_d['e-mail'] = 'hello@daum.net'
print(my_d)

# 삭제하기
del my_d['e-mail']
print(my_d)

# 키만 뽑아내기
print(list(my_d.keys()))

# 값만 추출
print(my_d.values())

# 키와 값의 쌍을 추출
print(my_d.items())

for k in my_d.keys():
    print(k)

# items()를 이용해서 my_d의 각 아이템의 키와 값을 출력
for x,y in my_d.items():
    print(x, y)

snack = {'산도':3000, '초코파이':4000, '영양갱':1000}
new_snack = {'고래밥':2000}
snack.update(new_snack)
print(snack)

str = 'hello'
str1 = str.capitalize()
print(str1)
print(str)

keys = ['아맛나','폴라포','땅크보이','바밤바']
vals = [600, 700, 1000, 500]
# for key, vals in zip(keys, vals):
#     print(key, vals)

my_dict2= dict(zip(keys,vals))
print(my_dict2)