def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def if_perfect_num(numbers):
    if len(numbers) > 985 and is_perfect_number(numbers[985]):
        return True
    return False