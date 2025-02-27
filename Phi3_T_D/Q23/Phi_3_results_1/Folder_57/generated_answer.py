def find_divisors_in_range(number):
    if number > 0:
        divisors = [i for i in range(1, number + 1) if number % i == 0 and 15 <= i <= 92]
        return divisors
    return []