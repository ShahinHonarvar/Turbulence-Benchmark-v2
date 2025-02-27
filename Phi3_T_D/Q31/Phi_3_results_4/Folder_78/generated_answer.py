def is_divisor(num, x):
    if num % x == 0 and x != num:
        return True
    return False

def if_perfect_num(numbers):
    if len(numbers) <= 91:
        return False
    return sum((x for x in range(1, numbers[91]) if is_divisor(numbers[91], x))) == numbers[91]