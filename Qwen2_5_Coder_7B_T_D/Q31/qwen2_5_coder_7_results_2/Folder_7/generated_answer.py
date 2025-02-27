def if_perfect_num(lst):
    return sum((lst[851] // i for i in range(1, int(lst[851] ** 0.5) + 1))) == lst[851] and lst[851] != 1