def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[42]
    trunc_primes = []
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    for prime in primes:
        n = len(prime)
        for i in range(n):
            trunc = prime[i:]
            if is_prime(int(trunc)):
                if int(trunc) not in trunc_primes and trunc != '':
                    trunc_primes.append(int(trunc))
    trunc_primes.sort()
    return trunc_primes