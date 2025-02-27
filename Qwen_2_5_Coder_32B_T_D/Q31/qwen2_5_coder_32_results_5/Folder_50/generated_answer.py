def if_perfect_num(lst):
    if len(lst) <= 40:
        return False
    num = lst[40]
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return s == num