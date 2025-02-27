from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True

    def truncatable_primes(n=0, threshold=x, names=[]):
        if isprime(n) and is_right_truncatable_prime(n) and (n < x):
            right_truncatable_primes.append(n)
            primes_list = [int(n[i:]) for i in range(len(str(n)))]
            for prime in primes_list:
                if prime >= 10 and prime not in names:
                    truncatable_primes(prime, threshold, names + [prime])
        return right_truncatable_primes
    return sorted(truncatable_primes(), reverse=True)