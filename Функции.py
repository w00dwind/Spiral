#lst = [1, 3, 5, 7]

#lst = [1, 2, 3, 4, 5, 6]
lst = [10, 5, 8, 3]
def modify_list(l):
    for i in reversed(range(len(l))):
        if l[i] % 2 != 0:
            del l[i]
        else: l[i] = l[i] // 2


modify_list(lst)
print(lst)               # [5, 4]