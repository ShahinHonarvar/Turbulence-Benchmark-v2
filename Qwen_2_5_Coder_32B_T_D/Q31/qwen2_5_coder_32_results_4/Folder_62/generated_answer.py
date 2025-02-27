def if_perfect_num(lst):
    if len(lst) > 926:
        num = lst[926]
        return num == sum((i for i in range(1, num) if num % i == 0))
    return False