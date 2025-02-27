def primes_sieve(limit):
    prime = [True] * limit
    prime[0] = prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit, i):
                prime[j] = False
    return prime

def is_left_truncatable_prime(n, prime):
    str_n = str(n)
    while len(str_n) > 0:
        if not prime[int(str_n)]:
            return False
        str_n = str_n[1:]
    return True

def all_left_truncatable_primes(numbers):
    limit = numbers[11] + 1
    prime = primes_sieve(limit)
    return [n for n in range(2, limit) if is_left_truncatable_prime(n, prime)]