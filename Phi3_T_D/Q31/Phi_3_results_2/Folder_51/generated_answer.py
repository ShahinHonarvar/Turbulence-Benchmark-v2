def is_perfect_num(numbers):
    if 64 < len(numbers) and sum((i for i in range(1, numbers[64]) if numbers[64] % i == 0)) == numbers[64]:
        return True
    return False