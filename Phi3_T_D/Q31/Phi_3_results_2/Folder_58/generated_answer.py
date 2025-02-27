def if_perfect_num(numbers):
    if len(numbers) > 714:
        div_sum = sum((i for i in range(1, numbers[714] // 2 + 1) if numbers[714] % i == 0))
        return div_sum == numbers[714]
    return False