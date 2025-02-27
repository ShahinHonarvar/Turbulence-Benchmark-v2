def find_divisors_in_range(number):
    divisors_in_range = []
    for i in range(18, 53):
        if number % i == 0:
            divisors_in_range.append(i)
    return divisors_in_range