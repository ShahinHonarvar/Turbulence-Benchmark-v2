def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    digits = str(n)
    if '0' in digits:
        return False
    for i in range(1, len(digits)):
        if not is_prime(int(digits[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)