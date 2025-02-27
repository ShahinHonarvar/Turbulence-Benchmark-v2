def if_perfect_num(numbers):

    def is_perfect(n):
        sum_factors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_factors += i + (n // i if i != n // i else 0)
        return sum_factors == n
    return is_perfect(numbers[96]) if len(numbers) > 96 else False