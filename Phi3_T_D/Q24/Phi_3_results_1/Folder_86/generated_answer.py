def sum_of_divisors_in_range(n):
    sum_divisors = sum((i for i in range(372, 495) if n % i == 0))
    return sum_divisors