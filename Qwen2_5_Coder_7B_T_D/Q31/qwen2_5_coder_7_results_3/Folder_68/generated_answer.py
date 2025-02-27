def if_perfect_num(lst):
    if len(lst) < 4:
        return False
    num = lst[3]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num