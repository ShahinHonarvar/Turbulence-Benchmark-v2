def find_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0 and i >= 50 and (i <= 84):
            divisors.append(i)
    return divisors