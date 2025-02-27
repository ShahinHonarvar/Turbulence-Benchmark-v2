from sympy import isprime

def get_truncatable_primes(upper_limit):
    primes = [str(num) for num in range(2, upper_limit + 1) if isprime(num)]
    truncatable_primes = []
    for prime in primes:
        if isprime(int(prime[1:])) and all((isprime(int(prime[:i])) for i in range(1, len(prime)))):
            truncatable_primes.append(int(prime))
    return sorted(truncatable_primes, reverse=True)

def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    return get_truncatable_primes(x)