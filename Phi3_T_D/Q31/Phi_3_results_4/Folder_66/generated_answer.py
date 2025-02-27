def if_perfect_num(lst):
    if len(lst) > 42:
        divisors_sum = sum((i for i in range(1, lst[42]) if lst[42] % i == 0))
        return divisors_sum == lst[42] or divisors_sum + lst[42] == lst[42]
    return False