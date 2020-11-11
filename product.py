

products = []
with open('products.csv', 'r', encoding = 'utf-8'):
	for line in f:
		if '商品,價格' in line:
			continue # 繼續
		name, price = line.strip().split(',')  # strip delete /n ; split切割完後結果是清單 restore name, price
		products.append([name , price])
print(products)

# 讓使用者輸入

while True:
	name = input('商品名稱：')
	if name == 'q':
		break
	price = input('商品價格：')
#	p = [name, price]
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for i in products:
	print(i[0], '的商品價格是:', i[1])

# 寫入coding 
with open('products.txt', 'w', encoding ='utf-8') as f:
	f.write('商品,價格\n') # \n下一行
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')  # ','可以做為區隔




