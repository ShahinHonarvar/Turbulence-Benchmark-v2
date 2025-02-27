def if_perfect_num(numbers):
    if len(numbers) <= 849:
        return False
    n = numbers[849]
    return sum((i for i in range(1, n) if n % i == 0)) == n