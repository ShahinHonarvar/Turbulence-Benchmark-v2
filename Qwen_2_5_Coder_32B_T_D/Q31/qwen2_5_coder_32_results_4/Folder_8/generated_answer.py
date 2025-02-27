def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = sum([d for d in range(1, n) if n % d == 0])
        return sum_divisors == n
    return is_perfect(numbers[49]) if len(numbers) > 49 else False