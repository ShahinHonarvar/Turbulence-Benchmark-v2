def if_perfect_num(lst):
    if len(lst) < 86:
        return False
    num = lst[85]
    s = sum((i for i in range(1, num) if num % i == 0))
    return s == num