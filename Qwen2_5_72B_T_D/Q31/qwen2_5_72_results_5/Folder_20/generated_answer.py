def if_perfect_num(numbers):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return is_perfect(numbers[53]) if len(numbers) > 53 else False