def if_perfect_num(numbers):
    if len(numbers) > 28:
        sum_of_divisors = sum((i for i in range(1, numbers[28]) if numbers[28] % i == 0))
        return sum_of_divisors == numbers[28] and sum_of_divisors != numbers[28] * 2
    else:
        return False