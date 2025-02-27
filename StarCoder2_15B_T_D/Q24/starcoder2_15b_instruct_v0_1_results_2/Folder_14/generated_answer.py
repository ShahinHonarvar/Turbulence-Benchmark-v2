def sum_of_divisors_in_range(num):
    if num < 1:
        raise ValueError('The input must be a positive integer.')
    sum_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and 6 <= i <= 8:
            sum_of_divisors += i
    return sum_of_divisors