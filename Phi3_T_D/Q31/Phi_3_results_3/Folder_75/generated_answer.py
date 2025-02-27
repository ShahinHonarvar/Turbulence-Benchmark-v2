def if_perfect_num(numbers):
    if len(numbers) > 80 and sum((i for i in range(1, numbers[80]) if numbers[80] % i == 0)) == numbers[80]:
        return True
    else:
        return False