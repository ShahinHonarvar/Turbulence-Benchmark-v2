def if_perfect_num(numbers):
    if len(numbers) > 84 and sum((i for i in range(1, numbers[84] // 2 + 1) if numbers[84] % i == 0)) == numbers[84]:
        return True
    return False