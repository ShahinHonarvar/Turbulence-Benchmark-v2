def find_divisors_in_range(number):
    divisors = [i for i in range(11, 57) if number % i == 0]
    return divisors