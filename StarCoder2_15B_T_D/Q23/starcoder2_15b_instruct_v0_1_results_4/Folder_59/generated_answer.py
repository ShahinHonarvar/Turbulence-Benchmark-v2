def find_divisors_in_range(num):
    return [i for i in range(1, num + 1) if num % i == 0 and 3 <= i <= 5]