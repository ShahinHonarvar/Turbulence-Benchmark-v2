def if_perfect_num(numbers):
    if len(numbers) <= 74:
        return False
    n = numbers[74]
    sum_divs = sum((d for d in range(1, n) if n % d == 0))
    return sum_divs == n