from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    left_truncatable_primes = []

    def is_left_truncatable(n):
        str_n = str(n)
        return all((isprime(int(str_n[i:])) for i in range(len(str_n)))) and str_n[0] != '0'
    current = 2
    while current < x:
        if is_left_truncatable(current):
            left_truncatable_primes.append(current)
        current += 1
    return left_truncatable_primes