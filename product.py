import os # operating system


def read_file(filename):
    products = [] # 無論找不找得到檔案 都要建立products list
    with open(filename, 'r', encoding = 'utf-8'):
        for line in f:
            if '商品,價格' in line:
                continue # 繼續
            name, price = line.strip().split(',')  # strip delete /n ; split切割完後結果是清單 restore name, price
            products.append([name , price])
    return products

# 讓使用者輸入
def use_input(products):
    while True:
        name = input('商品名稱：')
        if name == 'q':
            break
        price = input('商品價格：')
    #    p = [name, price]
        products.append([name, price])  #input商品後存在products,需要讓他出來
    print(products)
    return products

# 印出所有購買紀錄
def print_products(products):  # print something 不用回傳
    for i in products:
        print(i[0], '的商品價格是:', i[1])

# 寫入coding 
def write_file(filename, products):
    with open(filename, 'w', encoding ='utf-8') as f:
        f.write('商品,價格\n') # \n下一行
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')  # ','可以做為區隔


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # check wether the file exist or not
        print('yes! we found the file')
        products = read_file(products)
    else:
        print('cannot found the file')

    products = use_input(products)
    print_products(products)
    write_file('products.csv', products)

