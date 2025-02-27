def if_perfect_num(numbers):
    if len(numbers) > 7 and any((i < 0 for i in numbers)):
        return False
    perfect_sum = sum([i for i in range(1, numbers[7]) if numbers[7] % i == 0])
    return perfect_sum == numbers[7] * 2