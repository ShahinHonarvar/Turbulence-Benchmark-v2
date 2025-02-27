def if_perfect_num(lst):
    if len(lst) > 92:
        sum_divisors = sum([i for i in range(1, lst[92] // 2 + 1) if lst[92] % i == 0])
        return sum_divisors == lst[92]
    return False