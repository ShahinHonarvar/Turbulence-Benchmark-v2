def if_perfect_num(lst):
    if len(lst) > 126:
        sum_of_divisors = sum([i for i in range(1, lst[126]) if lst[126] % i == 0])
        return sum_of_divisors == lst[126]
    return False