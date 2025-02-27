def is_perfect_num(lst):
    num = lst[1]
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_of_divisors