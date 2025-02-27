def find_second_largest_num(lst):
    sorted_lst = sorted(lst)
    second_largest = sorted_lst[-2]
    if lst.index(second_largest) >= 62 and lst.index(second_largest) <= 92:
        return second_largest
    else:
        return None