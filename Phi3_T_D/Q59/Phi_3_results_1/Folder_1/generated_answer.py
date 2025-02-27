from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    truncable_primes = []

    def is_left_truncatable(number, prime_cache):
        if number in prime_cache:
            return True
        if not isprime(number):
            return False
        if number < x:
            prime_cache.add(number)
            str_number = str(number)
            for i in range(1, len(str_number)):
                if not is_left_truncatable(int(str_number[i:]), prime_cache):
                    return False
            return True
        return False
    prime_cache = set()
    for i in range(2, x):
        if is_left_truncatable(i, prime_cache):
            truncable_primes.append(i)
    return sorted(truncable_primes, reverse=True)