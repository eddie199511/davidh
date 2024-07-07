my_list = [1, 2, 3, 4, 5]

print(my_list)

# Counts the number of items with this value
print(my_list.count(2))

# Gets the index of the item with the specified value
print(my_list.index(3))

# Reverses the order of the list
my_list.reverse()

# print out the reversed list
print(my_list)

# Reverse the list back to its orginal order
my_list.reverse()

# Iterate through a list
for x in my_list:
    print(x)

# print the value at index 0
print(my_list[0])

# print the value of LAST index in the list
print(my_list[-1])

# sublist from index 1 to index 3 (NOT inclusive)
print(my_list[1:3])
