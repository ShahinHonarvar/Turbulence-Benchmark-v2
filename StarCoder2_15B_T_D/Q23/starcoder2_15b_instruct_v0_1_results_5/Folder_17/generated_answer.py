def find_divisors_in_range(number):
    divisors = []
    for i in range(2, number + 1):
        if number % i == 0 and 10 <= i <= 69:
            divisors.append(i)
    return divisors