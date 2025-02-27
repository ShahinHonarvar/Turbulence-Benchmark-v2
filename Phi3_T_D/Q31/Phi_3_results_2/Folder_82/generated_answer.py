def if_perfect_num(numbers):
    if len(numbers) > 83:
        perfect_sum = sum((i for i in range(1, numbers[83] // 2 + 1) if numbers[83] % i == 0))
        return perfect_sum == numbers[83]
    return False