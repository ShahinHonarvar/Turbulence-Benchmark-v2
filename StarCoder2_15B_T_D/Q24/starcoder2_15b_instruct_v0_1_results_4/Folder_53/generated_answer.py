def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for i in range(1, number + 1):
        if number % i == 0 and 4 <= i <= 9:
            sum_of_divisors += i
    return sum_of_divisors