def if_perfect_num(numbers):
    if len(numbers) > 28:
        divisors_sum = sum((i for i in range(1, numbers[28]) if numbers[28] % i == 0))
        return divisors_sum == numbers[28]
    return False