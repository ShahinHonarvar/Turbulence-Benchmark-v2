def if_perfect_num(numbers):
    if len(numbers) > 63:
        n = numbers[63]
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return False