def is_perfect_num(lst):
    if len(lst) > 162 and lst[162] > 1:
        sum_divisors = sum([i for i in range(1, lst[162]) if lst[162] % i == 0])
        return sum_divisors == lst[162]
    return False