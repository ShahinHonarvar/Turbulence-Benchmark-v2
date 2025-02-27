import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    primes = [2, 3, 5, 7]
    truncatable_primes = []

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not sympy.isprime(int(str_n[i:])) or not sympy.isprime(int(str_n[:-i])):
                return False
        return True
    for p in primes:
        if p > x:
            break
        if is_left_right_truncatable(p):
            truncatable_primes.append(p)
    candidate = 11
    while candidate <= x:
        if sympy.isprime(candidate):
            if is_left_right_truncatable(candidate):
                truncatable_primes.append(candidate)
        candidate += 2
    return sorted(truncatable_primes)