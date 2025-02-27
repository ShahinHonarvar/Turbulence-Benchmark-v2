def if_perfect_num(numbers):

    def is_perfect(n):
        return sum((i for i in range(1, n // 2 + 1) if n % i == 0)) == n
    return is_perfect(numbers[19]) if len(numbers) > 19 else False