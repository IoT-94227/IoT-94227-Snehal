text =input("Enter a string: ")
print("1.First 5 characters")
print("2.Last 5 characters")
print("3.Reverse string")
print("4.Characters at even index")
print("5.haracters at odd index")
choice=int(input("Enter your choice: "))
if choice==1:
    print(text[ :5])
elif choice==2:
    print(text[-5: ])
elif choice==3:
    print(text[::-1])
elif choice==4:
    print(text[::2])
elif choice==5:
    print(text[1::2 ])
else:
    print("Invalid choice")
