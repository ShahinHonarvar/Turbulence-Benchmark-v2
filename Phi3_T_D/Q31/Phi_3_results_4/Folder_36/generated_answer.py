def if_perfect_num(numbers):
    if len(numbers) < 991:
        return False
    num = numbers[990]
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return num == divisors_sum