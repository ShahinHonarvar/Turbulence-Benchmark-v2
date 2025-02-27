def find_divisors_in_range(number):
    divisors = [num for num in range(378, 783) if number % num == 0]
    return divisors