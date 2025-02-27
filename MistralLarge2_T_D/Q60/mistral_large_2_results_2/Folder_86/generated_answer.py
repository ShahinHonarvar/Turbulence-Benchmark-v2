def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if not is_prime(num) or '0' in str(num):
        return False
    s = str(num)
    for _ in range(len(s) - 1):
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[126]
    primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(primes, reverse=True)