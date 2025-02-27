def if_perfect_num(lst):
    return sum((lst[993] // i for i in range(1, lst[993]))) == lst[993]