def sum_of_divisors_in_range(num):
    divisors_sum = 0
    for i in range(7, 9):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum