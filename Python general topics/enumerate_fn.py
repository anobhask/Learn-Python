lst1 = ["eat", "sleep", "pray", "repeat", 8]

enum_list = enumerate(lst1)

print(enum_list)
print(list(enum_list))

list_iter = iter(lst1)
while list_iter:
    print(next(list_iter))
