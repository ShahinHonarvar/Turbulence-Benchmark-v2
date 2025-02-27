import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    truncatable_primes = []

    def is_truncatable_prime(n):
        str_n = str(n)
        return all((sympy.isprime(int(str_n[i:])) for i in range(1, len(str_n)))) and all((sympy.isprime(int(str_n[i:i + 2])) for i in range(len(str_n) - 1)))
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)