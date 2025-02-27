def if_perfect_num(numbers):
    if len(numbers) < 29:
        return False
    return sum([i for i in range(1, numbers[28]) if numbers[28] % i == 0]) == numbers[28]