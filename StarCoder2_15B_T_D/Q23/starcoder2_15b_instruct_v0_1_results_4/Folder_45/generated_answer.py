def find_divisors_in_range(number):
    divisors = []
    for i in range(2, number + 1):
        if number % i == 0 and i >= 4 and (i <= 8):
            divisors.append(i)
    return divisors