from sympy import isprime

def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True

    def generate_primes(limit):
        primes = []
        for num in range(2, limit + 1):
            if isprime(num) and '0' not in str(num):
                primes.append(num)
        return primes
    primes = generate_primes(x)
    truncatable_primes = [p for p in primes if is_left_right_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)