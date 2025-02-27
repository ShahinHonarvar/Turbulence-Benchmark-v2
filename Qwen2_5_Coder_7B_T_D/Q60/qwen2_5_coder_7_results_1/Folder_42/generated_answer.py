from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    truncatable_primes = []

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if int(str_n[i:]) not in primes or int(str_n[:i + 1]) not in primes:
                return False
        return True
    primes = [i for i in range(2, x + 1) if isprime(i) and '0' not in str(i)]
    for prime in primes:
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)