def if_perfect_num(lst):
    if 851 < len(lst):
        n = lst[851]
        sum_divisors = sum([x for x in range(1, n) if n % x == 0])
        return sum_divisors == n
    else:
        return False