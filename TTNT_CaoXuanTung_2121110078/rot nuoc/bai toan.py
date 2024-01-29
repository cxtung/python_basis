ketqua = float(input("Nhập kết quả: "))
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))


toantu = None


if ketqua == a + b:
    toantu = '+'

elif ketqua == a - b:
    toantu = '-'

elif ketqua == a * b:
    toantu = '*'

elif ketqua == a / b:
    toantu = '/'

elif ketqua == a // b:
    toantu = '//'
elif ketqua == a % b:
    toantu = '%'

elif ketqua == a ** b:
    toantu = 'khong tìm thấy dấu phù hợp'

else:
    print("Không tìm thấy dấu phù hợp cho kết quả đã cho.")
    exit()

print('Kết quả', ketqua ,'được đạt được bằng cách sử dụng dấu toán tử ',toantu)
print('phép toán là:',ketqua,'=',a,toantu,b)
