def if_perfect_num(numbers):

    def is_perfect(n):
        sum_factors = sum((i for i in range(1, n) if n % i == 0))
        return n == sum_factors
    return is_perfect(numbers[77]) if len(numbers) > 77 else False