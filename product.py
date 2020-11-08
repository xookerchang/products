products =[]
while True:
	name = input('商品名稱：')
	if name == 'q':
		break
	price = input('商品價格：')
#	p = [name, price]
	products.append([name, price])
print(products)

for i in products:
	print(i[0], '的商品價格是:', i[1])




