def is_perfect_num(lst):
    if len(lst) < 3 or lst[2] < 1:
        return False
    divisors_sum = sum([i for i in range(1, lst[2]) if lst[2] % i == 0])
    return divisors_sum == lst[2]