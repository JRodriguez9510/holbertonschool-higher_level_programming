#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list1 = my_list.copy()
    leng = len(my_list)
    if idx < 0:
        return list1
    if idx >= leng:
        return list1
    list1[idx] = element
    return list1
