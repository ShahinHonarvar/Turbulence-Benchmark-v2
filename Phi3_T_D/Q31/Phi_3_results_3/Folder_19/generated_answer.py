def is_perfect_num(numbers):
    if len(numbers) <= 13:
        return False
    return sum([i for i in range(1, numbers[13]) if numbers[13] % i == 0]) == numbers[13]