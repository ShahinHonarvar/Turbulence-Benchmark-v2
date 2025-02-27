def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_left_and_right_truncatable(n):
    if not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[18]
    primes = [i for i in range(2, x + 1) if is_left_and_right_truncatable(i)]
    return sorted(primes, reverse=True)