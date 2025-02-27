def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(2, num + 1):
        if num % i == 0 and 2 <= i <= 6:
            sum_of_divisors += i
    return sum_of_divisors