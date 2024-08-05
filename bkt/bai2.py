x = int(input("Nhap x = "))
while (x<0) :
    x = int(input("Nhap x = "))
if x <= 3 : print("so buoc toi thieu de rua ve dich la : ",1)
elif x % 3 == 0 : print("so buoc toi thieu de rua ve dich la : ",x/3)
else : print("so buoc toi thieu de rua ve dich la : ",x//3+1)


