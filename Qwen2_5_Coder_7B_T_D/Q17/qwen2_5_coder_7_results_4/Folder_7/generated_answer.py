def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(543, 585):
        if lst[i] % -553 == 0 and lst[i] % -737 == 0:
            result.append(lst[i])
    return result