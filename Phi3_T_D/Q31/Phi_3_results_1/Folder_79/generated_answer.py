def if_perfect_num(numbers):
    if len(numbers) > 63:
        perfection_sum = sum((i for i in range(1, numbers[63]) if numbers[63] % i == 0))
        return perfection_sum == numbers[63]
    return False