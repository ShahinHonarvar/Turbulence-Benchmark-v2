def if_perfect_num(numbers):
    if len(numbers) > 40:
        target_num = numbers[40]
        divisors_sum = sum((i for i in range(1, target_num) if target_num % i == 0))
        return divisors_sum == target_num
    return False