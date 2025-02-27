def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for i in range(3, 8):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors