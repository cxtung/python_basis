def checkve(gio,phut):
    if(gio==9 and phut>=30) or (9<gio<16) or (gio==16 and phut<=30):
        print('ve thường')
    elif(gio>=19) or (gio==7 and phut>=30):
        print("vé tiết kiệm")
    else:
        print("vé ko hợp lệ")

gio=int(input("nhập giờ:"))
phut=int(input("nhập phút:"))
checkve(gio,phut)