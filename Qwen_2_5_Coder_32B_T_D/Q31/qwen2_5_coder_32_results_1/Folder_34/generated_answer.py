def if_perfect_num(numbers):
    if len(numbers) < 98:
        return False
    n = numbers[97]
    return n == sum((i for i in range(1, n) if n % i == 0))