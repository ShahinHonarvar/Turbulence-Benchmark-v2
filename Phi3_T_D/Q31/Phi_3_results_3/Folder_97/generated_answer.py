def if_perfect_num(numbers):
    index = 132
    if index >= len(numbers):
        return False

    def is_perfect(n):
        sum_divisors = sum([x for x in range(1, n // 2 + 1) if n % x == 0])
        return n == sum_divisors
    return is_perfect(numbers[index])