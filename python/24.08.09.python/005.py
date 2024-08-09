# 올해의 년도는 2024. 이름과 태어난 년도를 입력받아 "홍길동 24세"와 같은 출력하시오
this_year = 2024
name = input('이름을 입력하세요 : ')
birth_year = int(input('태어난 년도를 입력하세요 : '))
old = this_year - birth_year
print(f'{name} {old}세') 