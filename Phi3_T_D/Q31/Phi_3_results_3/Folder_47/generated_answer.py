def if_perfect_num(numbers):
    if len(numbers) <= 34:
        return False
    target = numbers[34]
    divisors = [i for i in range(1, target) if target % i == 0]
    return sum(divisors) == target