def is_left_truncatable_prime(n, primes_set):
    str_n = str(n)
    for i in range(len(str_n)):
        if int(str_n[i:]) not in primes_set:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[24]
    primes = set()
    for n in range(2, x):
        if n not in primes and is_left_truncatable_prime(n, primes):
            primes.add(n)
    return sorted(primes)