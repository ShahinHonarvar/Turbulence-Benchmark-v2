def sum_of_divisors_in_range(number):
    divisors = [i for i in range(4, 10) if number % i == 0]
    return sum(divisors)