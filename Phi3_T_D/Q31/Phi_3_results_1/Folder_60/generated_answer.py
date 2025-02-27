def is_perfect_num(lst):
    if 88 < len(lst):
        number = lst[88]
        divisors_sum = sum([i for i in range(1, number) if number % i == 0])
        return divisors_sum == number
    return False