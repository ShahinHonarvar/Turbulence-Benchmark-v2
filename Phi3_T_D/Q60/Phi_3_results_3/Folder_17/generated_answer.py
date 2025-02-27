from sympy import isprime

def is_truncatable_prime(number):
    str_num = str(number)
    for i in range(1, len(str_num)):
        if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers_tup):
    x = numbers_tup[36]
    truncatable_primes = [prime for prime in range(2, x + 1) if is_truncatable_prime(prime)]
    return sorted(truncatable_primes, reverse=True)