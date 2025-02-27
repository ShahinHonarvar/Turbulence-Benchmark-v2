def if_perfect_num(numbers):
    if 51 < len(numbers):
        number = numbers[51]
        sum_of_divisors = sum((i for i in range(1, number) if number % i == 0))
        return sum_of_divisors == number
    else:
        return False