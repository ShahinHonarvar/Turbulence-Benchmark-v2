def sum_of_divisors_in_range(number):
    if number <= 0:
        return 0
    divisors = [i for i in range(472, 828) if number % i == 0]
    return sum(divisors)