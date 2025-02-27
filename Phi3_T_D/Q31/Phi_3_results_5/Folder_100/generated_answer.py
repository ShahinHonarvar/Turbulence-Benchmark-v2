def if_perfect_num(digits):
    if len(digits) <= 99:
        return False

    def is_perfect(n):
        divisors_sum = sum((i for i in range(1, n) if n % i == 0))
        return divisors_sum == n
    return is_perfect(digits[99])