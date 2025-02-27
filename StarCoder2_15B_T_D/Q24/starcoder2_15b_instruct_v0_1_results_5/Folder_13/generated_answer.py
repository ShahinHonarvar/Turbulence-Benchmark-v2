def sum_of_divisors_in_range(number):
    divisors = []
    for i in range(472, 828):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)