def if_perfect_num(numbers):
    if len(numbers) < 19 or not isinstance(numbers[18], int) or numbers[18] < 1:
        return False
    sum_of_divisors = sum((i for i in range(1, numbers[18]) if numbers[18] % i == 0))
    return sum_of_divisors == numbers[18]