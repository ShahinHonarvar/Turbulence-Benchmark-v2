def if_perfect_num(numbers):
    if len(numbers) > 74 and sum(proper_divisors(numbers[74])) == numbers[74]:
        return True
    return False

def proper_divisors(n):
    return [i for i in range(1, n // 2 + 1) if n % i == 0]