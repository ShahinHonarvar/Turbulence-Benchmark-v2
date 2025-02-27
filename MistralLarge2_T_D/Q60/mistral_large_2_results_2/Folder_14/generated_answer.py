def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if '0' in str(n):
        return False
    s = str(n)
    while len(s) > 1:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[78]
    primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)