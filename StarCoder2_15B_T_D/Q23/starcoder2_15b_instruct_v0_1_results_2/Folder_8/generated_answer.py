def find_divisors_in_range(number):
    divisors = []
    for divisor in range(1, number + 1):
        if 48 <= divisor <= 62 and number % divisor == 0:
            divisors.append(divisor)
    return divisors