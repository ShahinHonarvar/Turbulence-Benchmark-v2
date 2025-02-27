def if_perfect_num(numbers):
    perfect_sum = sum((i for i in range(1, 55) if 54 < len(numbers) and numbers[54] % i == 0)) - numbers[54]
    return perfect_sum == numbers[54] if 54 < len(numbers) else False