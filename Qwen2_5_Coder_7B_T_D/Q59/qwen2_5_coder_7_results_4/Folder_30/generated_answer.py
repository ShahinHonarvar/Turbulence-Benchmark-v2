from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        while str_prime:
            if not isprime(int(str_prime)):
                break
            str_prime = str_prime[1:]
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)