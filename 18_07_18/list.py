
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list)

print("Length of the list is ", len(my_list))

print(my_list[0])
print(my_list[5])
print(my_list[:4])
print(my_list[5:8])
print(my_list[:])


my_list.append(12)

print(my_list)

my_list[5] = 5

print(my_list)


my_list[5:9] = []

print(my_list)


my_list.insert(5, 8)
print(my_list)

my_list[2:5] = [6, 6, 6]
print(my_list)



my_list.remove(8)
print(my_list)



s = "Aditya Srivastava"

print(s[5])


s = s.split()

print(s)

print(len(s))