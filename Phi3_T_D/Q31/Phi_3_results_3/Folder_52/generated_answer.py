def if_perfect_num(numbers):
    if 478 < len(numbers):
        n = numbers[478]
        divisors = [i for i in range(1, n) if n % i == 0]
        return sum(divisors) == n
    return False