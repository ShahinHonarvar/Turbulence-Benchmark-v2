def if_perfect_num(lst):
    if len(lst) < 17:
        return False
    num = lst[16]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num