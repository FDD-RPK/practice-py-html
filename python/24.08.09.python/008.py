# if문
# 20세이상이면 성인, 아니면 미성년자

# 들여쓰기가 중괄호를 대신한다
old = int(input('나이를 입력하세요 : '))
if old>=20 and old<60 :
    print('성인입니다')
    print('한참 좋을 때네요')
elif old<20: 
    print('미성년자입니다')
    print('멀으셨군요')
else :
    print('어르신입니다')
    print('정중히모십니다')