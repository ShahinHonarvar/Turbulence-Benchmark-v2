def if_perfect_num(numbers):

    def is_perfect(n):
        s = sum((x for x in range(1, n) if n % x == 0))
        return s == n
    return is_perfect(numbers[41]) if len(numbers) > 41 else False