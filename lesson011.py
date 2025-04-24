
my_list = ["My name is Kevin!", 10, 4.5]

my_list[0] = "My name is Daniel"
my_list[1] = 15
for item in my_list:
    print(item)
print()

del my_list[0]
print(len(my_list))
print(my_list)
print()

my_list.append("This is a new item!")
my_list.append("This is the last item")
print(my_list)
print()

print(my_list[-1])
print(my_list[-2])
print(my_list[0:2])
print(25*'-')

list1 = [1, "This is the list1", 3.5]
list2 = [True, "This is the list2", False]
result = list1 + list2
print(result)

result = list1.extend(list2)
print(result)
print(list1)

list1.append('A new item')
print(list1)
result = list1.copy()
print(result)
list1.remove(3.5)
list1.remove("This is the list2")
print(list1)
result = list1.pop()
print(result)
print(list1)
list1.reverse()
print(list1)
print(25*'-')

list_names = ['Anna', 'Kevin', 'Stephen', 'Daniel', 'Adam', 'Joe', 'Maria', 'Adele']
print(list_names)
list_names.sort()
print(list_names)
print()

list_names = [45, 3, -5, 12, 15, 8, 7, 7,-5, 0, 1]
print(list_names)
list_names.sort()
print(list_names)
print()



