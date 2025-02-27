def find_primes_between_indices(numbers):
    primes = [n for n in numbers if isprime(n)]
    return sorted(primes[38:56], reverse=True)