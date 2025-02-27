def if_perfect_num(numbers):
    if len(numbers) == 0:
        return False
    num = numbers[0]
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    return sum_divisors == num