def if_perfect_num(lst):
    i = 99
    num = lst[i]
    sum_divisors = 0
    for j in range(1, num):
        if num % j == 0:
            sum_divisors += j
    return sum_divisors == num