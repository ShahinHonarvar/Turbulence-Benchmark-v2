def if_perfect_num(numbers):
    if len(numbers) > 68 and is_perfect_number(numbers[68]):
        return True
    else:
        return False

def is_perfect_number(n):
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n