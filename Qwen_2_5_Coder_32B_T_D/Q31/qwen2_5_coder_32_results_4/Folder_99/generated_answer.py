def if_perfect_num(numbers):
    if len(numbers) > 733:
        n = numbers[733]
        return n == sum((i for i in range(1, n) if n % i == 0))
    return False