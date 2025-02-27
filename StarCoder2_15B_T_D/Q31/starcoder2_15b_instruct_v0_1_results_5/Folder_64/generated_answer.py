def if_perfect_num(lst):
    if len(lst) < 2:
        return False
    num = lst[1]
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num