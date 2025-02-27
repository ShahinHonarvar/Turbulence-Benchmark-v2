def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[433]

    def is_left_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)