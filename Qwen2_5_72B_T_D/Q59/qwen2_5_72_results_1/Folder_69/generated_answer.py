from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[760]

    def is_left_truncatable_prime(n):
        return all((isprime(int(str(n)[i:])) for i in range(len(str(n)))))
    return [n for n in range(x - 1, 1, -1) if is_left_truncatable_prime(n) and '0' not in str(n)]