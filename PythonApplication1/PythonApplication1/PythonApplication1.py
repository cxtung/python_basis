khoa = int(input('nhap khoa:'));
bang = int(input('nhap bang:'));
nong = int(input('nhap nong:'));

c = 0


def tienhoahong(khoa,nong,bang):
    tong = (khoa * 45) + (bang * 30) + (nong * 25);
    if tong <= 1000:
        print('tien hoa hồng ', tong * (10 / 100));
    elif 1000 < tong < 1800:
        print('tien hoa hồng ', tong * (15 / 100));
    else:
        print('tien hoa hồng ', tong * (20 / 100));
if nong>0 and bang>0 and khoa>0:
    tienhoahong(khoa,nong,bang)
else:
    print('người bán không hợp lệ')