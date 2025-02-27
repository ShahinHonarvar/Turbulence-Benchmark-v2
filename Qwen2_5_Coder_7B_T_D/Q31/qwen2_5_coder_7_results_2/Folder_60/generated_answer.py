def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[88]) if numbers[88] % i == 0]) == numbers[88] if len(numbers) > 88 else False