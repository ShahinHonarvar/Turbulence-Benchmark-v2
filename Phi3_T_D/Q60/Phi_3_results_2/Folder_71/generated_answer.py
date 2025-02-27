from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    truncatable_primes = []

    def is_truncatable(n):
        str_n = str(n)
        if not str_n.startswith('0') and (not str_n.endswith('0')):
            for i in range(1, len(str_n)):
                if not isprime(int(str_n[i:])) or not isprime(int(str_n[:i])):
                    return False
            return isprime(n)
        return False
    for i in range(x, 1, -1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return truncatable_primes