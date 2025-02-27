def is_perfect_num(numbers):
    if len(numbers) > 40:
        return divisors_sum(numbers[40]) == 2 * numbers[40]
    return False

def divisors_sum(num):
    return sum((i for i in range(1, num) if num % i == 0))