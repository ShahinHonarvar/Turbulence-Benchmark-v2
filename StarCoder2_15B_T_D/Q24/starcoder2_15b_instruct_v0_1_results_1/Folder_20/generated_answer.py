def sum_of_divisors_in_range(num):
    return sum((i for i in range(1, num + 1) if num % i == 0 and 28 <= i <= 81))