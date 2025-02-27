def find_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0 and 15 <= i <= 92:
            divisors.append(i)
    return divisors