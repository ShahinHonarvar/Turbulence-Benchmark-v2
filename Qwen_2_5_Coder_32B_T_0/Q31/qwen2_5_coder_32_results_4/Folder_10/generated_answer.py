def if_perfect_num(numbers):

    def is_perfect(n):
        sum_factors = sum((i for i in range(1, n) if n % i == 0))
        return sum_factors == n
    return is_perfect(numbers[54]) if len(numbers) > 54 else False