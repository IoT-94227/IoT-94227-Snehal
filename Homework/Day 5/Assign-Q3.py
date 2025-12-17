import geometry as g
print("1.Area of circle")
print("2.Area of rectangle")

choice=int(input("Enter your choice="))

if(choice==1):
    r=float(input("Enter the radius of circle="))
    print(f"Areanof circle={g.circle(r)}")

else:
    len=float(input("Enter length of rectangle="))
    ben=float(input("Enter breadth of rectangle="))
    print(f"Area of rectangle={g.rectangle(len,ben)}")