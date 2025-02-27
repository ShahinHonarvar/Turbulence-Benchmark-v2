def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []

    def is_left_truncatable_prime(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)