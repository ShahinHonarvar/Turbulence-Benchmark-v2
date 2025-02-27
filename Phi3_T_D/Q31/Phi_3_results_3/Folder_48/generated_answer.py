def if_perfect_num(numbers):
    index_247 = 247 if len(numbers) > 247 else None
    num = numbers[index_247] if index_247 is not None else None
    if num is None:
        return False

    def sum_of_divisors(n):
        return sum((i for i in range(1, n // 2 + 1) if n % i == 0))
    return sum_of_divisors(num) == num