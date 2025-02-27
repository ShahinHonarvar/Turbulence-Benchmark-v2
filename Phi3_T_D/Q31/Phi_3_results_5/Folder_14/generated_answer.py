def if_perfect_num(num_list):
    if len(num_list) <= 17:
        return False
    n = num_list[17]
    divisors_sum = sum([x for x in range(1, n) if n % x == 0])
    return divisors_sum == n