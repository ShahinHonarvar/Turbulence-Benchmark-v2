def if_perfect_num(numbers):
    if len(numbers) < 46:
        return False
    n = numbers[45]
    sum_div = sum((i for i in range(1, n) if n % i == 0))
    return sum_div == n