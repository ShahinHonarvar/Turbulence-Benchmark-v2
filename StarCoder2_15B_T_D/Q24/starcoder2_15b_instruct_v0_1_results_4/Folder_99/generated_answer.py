def sum_of_divisors_in_range(num):
    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0 and 378 <= i <= 782:
            divisors_sum += i
    return divisors_sum