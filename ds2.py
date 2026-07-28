#add list preform use operation
number=[10,20,30,40,50]
print("Original list:", number)
number.insert(3,25)
print("List after insertion:", number)
number.remove(20)
print("List after deletion:", number)
number[1]=100
print("List after modification:", number)