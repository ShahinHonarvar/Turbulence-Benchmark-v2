def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and 1 <= i <= 9:
            sum_of_divisors += i
    return sum_of_divisors