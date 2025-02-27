def if_perfect_num(numbers):
    if 162 < len(numbers):
        num = numbers[162]
        divisors_sum = sum((i for i in range(1, num // 2 + 1) if num % i == 0))
        return divisors_sum == num
    return False