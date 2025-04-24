my_list = [1,5,10,5]

print(my_list[0])
print(my_list[1])
print(my_list[2])
#print(my_list[10])
print()

my_list = list((1,5,10,5))

print(my_list[0])
print(my_list[1])
print(my_list[2])
print()

my_list = ["My name is Kevin!", 10, 4.5]

print(my_list[0])
print(my_list[1])
print(my_list[2])
print()

for item in my_list:
    print(item)
print()

print(len(my_list))
print(type(my_list))

my_list[0] = "My name is Daniel"
my_list[1] = 15
for item in my_list:
    print(item)
print()

del my_list[0]
print(len(my_list))
print(my_list)
print()
