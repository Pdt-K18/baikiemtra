n = int(input("n = "))
diem=[]
ten=[]
for i in range(n) : 
    a = str(input("Ten :"))
    ten.append(a)
    b = int(input("So diem dat duoc : "))
    diem.append(b)
f=min(diem)
for i in range(n) :
    if (f==diem[i]) :
        print("Ten ban co so diem thap nhat la : ",ten[i])    
