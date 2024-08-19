icecream_price = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream_price)

icecream_price['죠스바'] = 1200
icecream_price['월드콘'] = 1500
print(icecream_price)

print('메로나 가격 :', icecream_price['메로나'], '원')

icecream_price['메로나'] = 1300
print(icecream_price)

del icecream_price['메로나']
print(icecream_price)

price = {'메로나':1000, '폴라포':1200}
box = {'메로나':10, '폴라포':3}
print(price, box)

print('메로나', price['메로나'], '재고', box['메로나'])
print('폴라포', price['폴라포'], '재고', box['폴라포'])

box['폴라포'] = 2
print(box)
