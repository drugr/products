
import os # operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):
	print('yeah!!程式啟動~~')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			# s = line.strip().split(',') #切割split，裡面放你想要用什麼來分割，這邊是 "，"；strip是去掉 "\n"
			# name = s[0]
			# price = s[1]
			if '商品,價格' in line:
				continue #continue是跳到下一回的意思
			name, price = line.strip().split(',')
			products.append([name, price])
			print([name, price])
			# # split 完的結果是 清單 list
else:
	print('找不到檔案......')

#讓使用者輸入新的商品		
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
#列出清單
print(products)
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #f.write 寫入 