def if_perfect_num(lst):
    sum_of_divisors = 0
    for i in range(1, lst[0]):
        if lst[0] % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == lst[0]