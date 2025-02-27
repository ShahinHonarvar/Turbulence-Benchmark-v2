def if_perfect_num(lst):
    if len(lst) <= 263:
        return False
    num = lst[263]
    return num == sum((i for i in range(1, num) if num % i == 0))