def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = [n for n in range(2, x) if is_prime(n) and '0' not in str(n)]
    left_truncatable_primes = []
    for prime in primes:
        num = prime
        while num > 0:
            if not is_prime(num):
                break
            num = int(str(num)[1:])
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)