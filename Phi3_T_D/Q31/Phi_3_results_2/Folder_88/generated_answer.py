def if_perfect_num(numbers):
    if len(numbers) > 46:
        return sum((i for i in range(1, numbers[46]) if numbers[46] % i == 0)) == numbers[46] * 2
    return False