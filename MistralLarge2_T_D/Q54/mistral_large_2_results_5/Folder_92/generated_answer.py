def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    truncatable_primes = [2, 3, 5, 7]
    while primes:
        prime = primes.pop(0)
        for digit in ['1', '3', '7', '9']:
            num = int(str(prime) + digit)
            if num < x and is_prime(num):
                primes.append(num)
                truncatable_primes.append(num)
    return sorted(set(truncatable_primes))