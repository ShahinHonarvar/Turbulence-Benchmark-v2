def if_perfect_num(numbers):
    if len(numbers) < 75:
        return False
    n = numbers[74]
    return n == sum((x for x in range(1, n) if n % x == 0))