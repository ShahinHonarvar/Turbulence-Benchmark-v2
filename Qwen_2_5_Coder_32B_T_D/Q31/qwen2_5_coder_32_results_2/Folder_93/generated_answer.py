def if_perfect_num(numbers):

    def is_perfect(n):
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    if len(numbers) < 46:
        return False
    return is_perfect(numbers[45])