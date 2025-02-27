def if_perfect_num(lst):
    if 24 < len(lst) and lst[24] > 0:
        divisors_sum = sum([i for i in range(1, lst[24]) if lst[24] % i == 0])
        return divisors_sum == lst[24]
    return False