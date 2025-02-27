from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[69]
    left_truncatable_primes = []

    def _is_truncatable(n, check_set):
        if n in check_set or not isprime(n):
            return False
        check_set.add(n)
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
        return True
    for num in range(x - 1, 1, -1):
        if _is_truncatable(num, set()):
            left_truncatable_primes.append(num)
    return left_truncatable_primes