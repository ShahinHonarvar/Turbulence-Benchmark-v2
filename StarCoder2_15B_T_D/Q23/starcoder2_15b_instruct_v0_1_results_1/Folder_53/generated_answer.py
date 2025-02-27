def find_divisors_in_range(number):
    divisors = []
    for i in range(2, number + 1):
        if number % i == 0 and 4 <= i <= 9:
            divisors.append(i)
    return divisors