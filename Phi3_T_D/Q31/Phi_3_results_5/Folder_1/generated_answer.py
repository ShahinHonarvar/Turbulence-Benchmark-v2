def is_perfect_num(perfects):
    num_to_check = perfects[85]
    sum_of_divisors = sum((i for i in range(1, num_to_check) if num_to_check % i == 0))
    return sum_of_divisors == num_to_check