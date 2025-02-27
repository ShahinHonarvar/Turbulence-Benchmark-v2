def if_perfect_num(numbers):
    if len(numbers) > 41 and sum((i for i in range(1, numbers[41]) if numbers[41] % i == 0)) == numbers[41]:
        return True
    return False