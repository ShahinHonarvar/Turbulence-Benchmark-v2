def if_perfect_num(positive_ints):
    if len(positive_ints) > 74:
        proper_divisors_sum = sum((i for i in range(1, positive_ints[74] // 2 + 1) if positive_ints[74] % i == 0))
        return proper_divisors_sum == positive_ints[74]
    return False