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

def all_left_right_truncatable_prime(numbers):
    x = numbers[89]
    primes = []

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        s = str(num)
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)