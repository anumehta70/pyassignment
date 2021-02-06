n=[]
for i in range(0,5):
    n.append(int(input(f"enter a {i+1} no.")))
a=n[0]+n[3]
b=a*n[4]
if b>100:
    print("greater than 100")
else:
    print("not greater than 100")
