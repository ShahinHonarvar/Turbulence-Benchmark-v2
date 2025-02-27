def if_perfect_num(lst):
    try:
        candidate = lst[701]
        divisors_sum = sum((i for i in range(1, candidate) if candidate % i == 0))
        return divisors_sum == candidate
    except IndexError:
        return False