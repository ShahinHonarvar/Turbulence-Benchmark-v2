def if_perfect_num(numbers):
    if len(numbers) < 35:
        return False
    num = numbers[34]
    divisors_sum = sum((d for d in range(1, num) if num % d == 0))
    return divisors_sum == num