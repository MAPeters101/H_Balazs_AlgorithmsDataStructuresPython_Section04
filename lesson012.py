numbers = [1, -5, 0, 10, 100, 67, 55, 20, 34]

new_list = []
for num in numbers:
    if num%2 == 0:
        new_list.append(num)
print(new_list)

new_list2 = [num for num in numbers if num%2 == 0]
print(new_list2)

names = ['Adam', 'Kevin', 'Anna', 'Joe', 'Daniel', 'Bill']
filtered_names = []
for name in names:
    if name.startswith('A'):
        filtered_names.append(name)
print(filtered_names)

filtered_names2 = [name for name in names if name.startswith('A')]
print(filtered_names2)

filtered_names3 = [name for name in names if len(name) == 4]
print(filtered_names3)


