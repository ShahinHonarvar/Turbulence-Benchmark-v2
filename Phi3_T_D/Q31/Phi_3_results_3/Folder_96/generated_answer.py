def is_perfect(n):
    divisors = [x for x in range(1, n // 2 + 1) if n % x == 0]
    return sum(divisors) == n

def if_perfect_num(numbers):
    if len(numbers) > 47:
        return is_perfect(numbers[47])
    else:
        return False