def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    left_truncatable_primes = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        is_left_truncatable = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return left_truncatable_primes