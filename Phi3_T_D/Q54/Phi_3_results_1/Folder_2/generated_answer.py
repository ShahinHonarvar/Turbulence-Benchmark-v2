def primes_sieve(limit):
    prime = [True] * limit
    prime[0] = prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit, i):
                prime[j] = False
    return prime

def is_right_truncatable_prime(number, prime_set):
    while number > 0:
        if not prime_set.get(number, False):
            return False
        number //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[618]
    if x < 11:
        return []
    prime_sieve = primes_sieve(x)
    right_truncatable_primes = []
    for number in range(11, x):
        if is_right_truncatable_prime(number, dict.fromkeys(prime_sieve)):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)