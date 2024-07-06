import os #operating system

#讀取檔案
protucts = []
if os.path.isfile('products.csv'):#檢查檔案在不在
	print('找到檔案了')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			protucts.append([name, price])
	print(protucts)

else:
	print('找不到檔案...')

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	protucts.append([name, price])
print(protucts)

#印出所有購買紀錄
for p in protucts:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in protucts:
		f.write(p[0] + ',' + p[1] + '\n')