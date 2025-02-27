def if_perfect_num(numbers):

    def is_perfect(n):
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    return is_perfect(numbers[27]) if len(numbers) > 27 else False