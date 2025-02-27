def sum_of_divisors_in_range(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError('Argument must be a positive integer')
    sum_of_divisors = sum((i for i in range(372, 495) if number % i == 0))
    return sum_of_divisors