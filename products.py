
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') #入果輸入q，就不用問價格了
	## p = []
	## p.append(name)
	## p.append(price)
	# p = [name, price]
	# products.append(p)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])