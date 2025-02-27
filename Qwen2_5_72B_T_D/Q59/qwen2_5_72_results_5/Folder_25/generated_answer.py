from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[92]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n)) + 1):
            if not isprime(int(str(n)[:i])):
                return False
        return True
    primes = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(primes)