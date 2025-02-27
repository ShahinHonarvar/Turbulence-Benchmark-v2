def if_perfect_num(numbers):
    if len(numbers) < 8:
        return False
    number = numbers[7]
    if number == 6 or number == 28:
        return True
    sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
    return sum_of_divisors == number