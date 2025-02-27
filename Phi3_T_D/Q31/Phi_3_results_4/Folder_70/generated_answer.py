def if_perfect_num(numbers):

    def is_perfect(n):
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    try:
        return is_perfect(numbers[845])
    except IndexError:
        return False