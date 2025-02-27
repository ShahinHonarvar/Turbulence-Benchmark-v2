def if_perfect_num(numbers):
    if len(numbers) > 459:
        sum_of_divisors = sum([i for i in range(1, numbers[459] // 2 + 1) if numbers[459] % i == 0])
        return sum_of_divisors == numbers[459]
    return False