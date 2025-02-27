def if_perfect_num(numbers):
    if len(numbers) < 9:
        return False
    return sum((i for i in range(1, numbers[8]) if numbers[8] % i == 0)) == numbers[8]