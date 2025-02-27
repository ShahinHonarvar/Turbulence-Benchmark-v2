def if_perfect_num(numbers):

    def is_perfect(n):
        sum_factors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_factors += i + n // i
        return sum_factors == n
    return is_perfect(numbers[2]) if len(numbers) > 2 else False