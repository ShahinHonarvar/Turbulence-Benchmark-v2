def if_perfect_num(numbers):
    if len(numbers) <= 69:
        raise IndexError('List must have at least 70 items to access index 69.')

    def is_perfect_number(n):
        sum_of_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_of_divisors == n
    return is_perfect_number(numbers[69])