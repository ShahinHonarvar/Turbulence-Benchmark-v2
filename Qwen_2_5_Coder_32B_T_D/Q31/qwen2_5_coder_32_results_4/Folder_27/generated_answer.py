def if_perfect_num(numbers):

    def is_perfect(n):
        return n == sum((x for x in range(1, n) if n % x == 0))
    return is_perfect(numbers[56]) if len(numbers) > 56 else False