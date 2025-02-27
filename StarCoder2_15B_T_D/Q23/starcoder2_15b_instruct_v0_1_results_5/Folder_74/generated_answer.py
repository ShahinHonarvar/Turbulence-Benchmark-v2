def find_divisors_in_range(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0 and 40 <= i <= 74:
            divisors.append(i)
    return divisors