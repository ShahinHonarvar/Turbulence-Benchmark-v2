def if_perfect_num(lst):
    if len(lst) > 35:
        divisors_sum = sum([i for i in range(1, lst[35]) if lst[35] % i == 0])
        return divisors_sum == lst[35]
    else:
        return False