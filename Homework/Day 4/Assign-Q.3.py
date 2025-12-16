def function_overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1=input("Enter the element in first list: ")
list2=input("Enter the element in second list: ")

if function_overlapping(list1, list2):
    print("At list one common element in least")
else :
     print("No common element in least")