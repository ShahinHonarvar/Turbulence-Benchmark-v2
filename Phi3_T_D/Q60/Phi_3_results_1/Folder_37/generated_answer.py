import sympy

def all_left_right_truncatable_prime(integers):
    x = integers[35]
    left_right_primes = []
    for i in range(x, 1, -1):
        str_i = str(i)
        if all((sympy.isprime(int(str_i[j:])) for j in range(len(str_i)))) and sympy.isprime(i):
            left_right_primes.append(i)
    return left_right_primes