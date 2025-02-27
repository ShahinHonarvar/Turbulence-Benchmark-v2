def if_perfect_num(numbers):
    if len(numbers) > 23:
        num = numbers[23]
        sum_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_divisors == num
    return False