from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        str_n = str(n)
        if len(str_n) == 1:
            return False
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:i + 1])):
                return False
        return True
    x = numbers[835]
    primes = [p for p in range(2, x + 1) if isprime(p)]
    truncatables = filter(is_truncatable, set(primes))
    return sorted(list(truncatables))