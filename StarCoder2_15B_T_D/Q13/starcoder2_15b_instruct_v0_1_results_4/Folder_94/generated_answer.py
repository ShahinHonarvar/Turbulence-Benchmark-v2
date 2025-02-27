def find_second_largest_num(lst):
    sorted_lst = sorted(lst)
    second_largest = sorted_lst[-2]
    if second_largest >= lst[28] and second_largest <= lst[40]:
        return second_largest
    else:
        return None