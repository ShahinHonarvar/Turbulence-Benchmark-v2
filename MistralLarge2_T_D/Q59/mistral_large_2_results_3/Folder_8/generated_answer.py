def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(num):
        s = str(num)
        while s:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
        return True
    x = numbers[41]
    primes = [num for num in range(2, x) if is_prime(num)]
    left_truncatable_primes = [num for num in primes if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes, reverse=True)