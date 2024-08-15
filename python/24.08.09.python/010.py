# 성적을 입력받아 100점은 수석, 90점이상은 A, 80점이상은 B, 70점이상은 C, 60점이상은 D, 아니면 F

# 국어와 영어 성적을 입력받아 모두 70점이상이면 합격, 아니면 불합격

# 국어와 영어 성적을 입력바당 모두 70점이상이면 우수, 하나라도 70점이상이면 합격, 아니면 불합격


result1 = int(input('성적을 입력하세요 : '))
if result1==100 : 
    print('수석입니다')
elif result1>=90 and result1<100 :
    print('A입니다')
elif result1>=80 and result1<90 :
    print('B입니다')
elif result1>=70 and result1<80 :
    print('C입니다')
elif result1>=60 and result1<70 :
    print('D입니다')
else :
    print('F입니다 수고하세요')

result2L = int(input('국어 점수를 입력하세요 : '))
result2E = int(input('영어 점수를 입력하세요 : '))
if result2L>=70 and result2E>=70 :
    print('합격입니다')
else :
    print('불합격입니다 나가세요')

result3L = int(input('국어 점수를 입력하세요 : '))
result3E = int(input('영어 점수를 입력하세요 : '))
if result3L>=70 and result3E>=70 :
    print('합격입니다 우수하시군요')
elif result3L>=70 or result3E>=70 :
    print('합격입니다')
else :
    print('불합격입니다 나가세요')