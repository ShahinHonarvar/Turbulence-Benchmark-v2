def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0
    divisors_sum = sum((i for i in range(43, 47) if num % i == 0))
    return divisors_sum