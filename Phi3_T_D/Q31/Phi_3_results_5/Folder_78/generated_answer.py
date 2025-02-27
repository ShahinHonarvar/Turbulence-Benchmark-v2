def is_perfect_num(lst):
    if len(lst) > 91 and lst[91] > 1:
        sum_of_divisors = sum((i for i in range(1, lst[91]) if lst[91] % i == 0))
        return sum_of_divisors == lst[91]
    return False