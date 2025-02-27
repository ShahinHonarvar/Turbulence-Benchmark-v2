def if_perfect_num(numbers):
    if len(numbers) <= 80:
        return False

    def is_perfect(n):
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    return is_perfect(numbers[80])