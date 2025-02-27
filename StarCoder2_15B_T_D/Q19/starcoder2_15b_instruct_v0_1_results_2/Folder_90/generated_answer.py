def all_ints_not_div_by_num(lst):
    output = []
    for i in range(767, 905):
        if lst[i] % -430 != 0:
            output.append(lst[i])
    return output