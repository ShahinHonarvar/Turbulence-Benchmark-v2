def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if not all((digit in ['2', '3', '5', '7'] for digit in str(n))) or not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_number = numbers[992]
    result = []
    for number in range(10, max_number + 1):
        if is_truncatable(number):
            result.append(number)
    return result