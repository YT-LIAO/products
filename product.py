import os #operating system

#讀取檔案
def read_file(filename):
	protucts = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',')
			protucts.append([name, price])
	return protucts

#讓使用者輸入
def user_file(protucts):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		protucts.append([name, price])
	print(protucts)
	return protucts

#印出所有購買紀錄
def print_prodicts(protucts):
	for p in protucts:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, protucts):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in protucts:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案在不在
		print('找到檔案了')
		protucts = read_file(filename)
	else:
		print('找不到檔案')

	products = user_file(protucts)
	print_prodicts(protucts)
	write_file('products.csv', protucts)

main()
