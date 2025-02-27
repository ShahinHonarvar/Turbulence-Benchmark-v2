def if_perfect_num(numbers):
    if len(numbers) < 74:
        return False
    n = numbers[73]
    sum_factors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_factors += i + n // i
    return n == sum_factors