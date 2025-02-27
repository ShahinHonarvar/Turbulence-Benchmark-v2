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
    x = numbers[992]
    primes = []

    def is_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        left, right = (s, s)
        while left:
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
            left = left[1:]
            right = right[:-1]
        return True
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i):
            primes.append(i)
    return sorted(primes)