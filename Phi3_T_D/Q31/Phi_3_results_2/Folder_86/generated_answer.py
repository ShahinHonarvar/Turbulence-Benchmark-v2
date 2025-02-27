def if_perfect_num(numbers):
    if len(numbers) > 194 and is_perfect(numbers[194]):
        return True
    return False

def is_perfect(num):
    sum_divisors = sum([i for i in range(1, num // 2 + 1) if num % i == 0])
    return num == sum_divisors