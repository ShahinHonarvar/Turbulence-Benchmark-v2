import sympy as sp

def all_right_truncatable_prime(numbers):
    x = numbers[73]
    result = []

    def is_right_truncatable_prime(p):
        str_p = str(p)
        return all((sp.isprime(int(str_p[:len(str_p) - i])) for i in range(len(str_p))))
    for i in range(x - 1, 1, -1):
        if sp.isprime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return result