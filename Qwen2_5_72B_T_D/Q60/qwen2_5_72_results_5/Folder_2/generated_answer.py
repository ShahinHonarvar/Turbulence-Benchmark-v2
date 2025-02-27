import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[618] if len(numbers) > 618 else 0
    if x < 2:
        return []
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num) or not is_prime(num):
            continue
        truncatable = True
        for i in range(1, len(str(num))):
            left_truncated = int(str(num)[i:])
            right_truncated = int(str(num)[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                truncatable = False
                break
        if truncatable:
            primes.append(num)
    return sorted(primes)