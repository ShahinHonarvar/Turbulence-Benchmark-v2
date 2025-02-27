def if_perfect_num(numbers):

    def is_perfect(n):
        sum_of_divisors = sum((d for d in range(1, n) if n % d == 0))
        return sum_of_divisors == n
    return 0 <= 56 < len(numbers) and is_perfect(numbers[56])