def if_perfect_num(numbers):
    if 632 >= len(numbers):
        return False
    n = numbers[632]
    sum_of_divisors = sum((i for i in range(1, n) if n % i == 0))
    return sum_of_divisors == n