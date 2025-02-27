def if_perfect_num(numbers):
    if len(numbers) > 537:
        div_sum = sum((i for i in range(1, numbers[537]) if numbers[537] % i == 0))
        return div_sum == numbers[537]
    return False