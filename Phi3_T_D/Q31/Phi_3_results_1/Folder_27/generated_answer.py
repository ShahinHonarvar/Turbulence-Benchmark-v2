def if_perfect_num(numbers):
    if len(numbers) > 56:
        def_sum = sum([i for i in range(1, numbers[56]) if numbers[56] % i == 0])
        return def_sum == numbers[56]
    return False