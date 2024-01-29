Vx=int(input("Nhap Vx:"))
Vy=int(input("Nhap Vy:"))
z=int(input("Nhap z:"))
x=0
y=0
if Vx >= Vy:
    while(x!=z and y!=z):
            if x==0:
                x=Vx;
                print("- Đổ đầy bình X (x=",x,", y=",y,")")
            elif y==Vy:
                y=0;
                print("Đổ hết nước trong bình Y (x=",x,", y=",y,")")
            elif x>0 and y<Vy:
                k=min(Vy-y,x)
                x=x-k;
                y=y+k;
                print("- Đổ nước từ bình X qua Y (x=",x,", y=",y,")");
else:
        while(x!=z and y!=z):
            if x==Vx:
                x=0;
                print("- Đổ hết nước trong bình X (x=",x,", y=",y,")")
            elif y==0:
                y=Vy;
                print("- Đổ đầy bình Y (x=",x,", y=",y,")")
            elif x<Vx and y>0:
                k=min(Vx-x,y)
                x=x+k;
                y=y-k;
                print("- Đổ nước từ bình Y qua X (x=",x,", y=",y,")");