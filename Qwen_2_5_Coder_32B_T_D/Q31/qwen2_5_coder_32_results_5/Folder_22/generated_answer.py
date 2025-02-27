def if_perfect_num(numbers):
    if len(numbers) > 72:
        n = numbers[72]
        return sum((i for i in range(1, n) if n % i == 0)) == n
    return False