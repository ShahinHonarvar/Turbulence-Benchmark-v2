def is_perfect_num(lst):
    n = 790
    if n >= len(lst):
        return False
    num = lst[n]
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    return num == sum_of_divisors