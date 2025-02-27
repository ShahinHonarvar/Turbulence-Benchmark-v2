def find_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0 and i in range(18, 53):
            divisors.append(i)
    return divisors