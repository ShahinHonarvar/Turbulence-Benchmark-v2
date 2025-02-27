def if_perfect_num(lst):
    return sum((lst[87] if i == 87 else 0 for i in range(lst[87] + 1))) == lst[87] and lst[87] != 1