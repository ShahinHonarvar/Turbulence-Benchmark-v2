def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[65]
    lr_truncatable_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' in s:
            continue
        truncatable = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                truncatable = False
                break
        if truncatable and is_prime(num):
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)