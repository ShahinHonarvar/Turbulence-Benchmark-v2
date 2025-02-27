def if_perfect_num(lst):
    if len(lst) <= 312:
        return False
    num = lst[312]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num