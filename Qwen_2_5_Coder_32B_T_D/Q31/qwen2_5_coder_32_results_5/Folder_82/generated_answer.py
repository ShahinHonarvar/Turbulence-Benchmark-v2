def if_perfect_num(numbers):

    def is_perfect(n):
        sum_of_divisors = sum((d for d in range(1, n) if n % d == 0))
        return sum_of_divisors == n
    return is_perfect(numbers[83]) if len(numbers) > 83 else False