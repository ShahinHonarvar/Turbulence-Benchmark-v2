def if_perfect_num(lst):
    perfect = sum([div for div in range(1, lst[3]) if lst[3] % div == 0]) == lst[3]
    return perfect