def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    truncatable_primes = []

    def is_truncatable_prime(n):
        if not is_prime(n) or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if '0' in s or not is_prime(int(s)):
                return False
        return True
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)