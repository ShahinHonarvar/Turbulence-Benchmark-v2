def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[758]
    right_truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        while s and all((is_prime(int(s[:i])) for i in range(1, len(s) + 1))):
            if is_prime(int(s)):
                right_truncatable_primes.append(int(s))
                break
            s = s[:-1]
    return sorted(right_truncatable_primes)