def if_perfect_num(numbers):
    if len(numbers) > 10:
        number = numbers[10]
        sum_divisors = sum((i for i in range(1, number) if number % i == 0))
        return sum_divisors == number
    return False