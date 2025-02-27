def is_perfect_num(num):
    """Check if a number is perfect."""
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    return sum_divisors == num

def if_perfect_num(numbers):
    if len(numbers) > 73:
        return is_perfect_num(numbers[73])
    else:
        return False