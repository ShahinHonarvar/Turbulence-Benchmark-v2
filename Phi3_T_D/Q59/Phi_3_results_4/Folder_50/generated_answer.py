def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if n < 10 or not is_prime(n):
        return False
    prev_prime = n % 10
    while n > 0:
        if not is_prime(n):
            return False
        prev_prime = n % 10
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[57]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)