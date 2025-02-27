from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:i])):
                return False
        return True
    x = numbers[87]
    truncatable_primes = [i for i in range(2, x + 1) if is_truncatable_prime(i)]
    return truncatable_primes