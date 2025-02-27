def if_perfect_num(lst):
    if len(lst) > 685 and lst[685] > 1:
        divisors_sum = sum([x for x in range(1, lst[685]) if lst[685] % x == 0])
        return divisors_sum == lst[685]
    return False