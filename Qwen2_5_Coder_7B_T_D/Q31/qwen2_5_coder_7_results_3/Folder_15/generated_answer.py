def if_perfect_num(num_list):
    if len(num_list) > 10:
        candidate = num_list[10]
        sum_of_divisors = sum((i for i in range(1, candidate) if candidate % i == 0))
        return sum_of_divisors == candidate
    return False