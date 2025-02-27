from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def truncatable(n):
        return all((isprime(int(str(n)[:i] + str(n)[i + 1:])) for i in range(len(str(n)))))
    x = numbers[759]
    result = []
    for prime in filter(isprime, range(2, x + 1)):
        if truncatable(prime):
            result.append(prime)
    return sorted(result, reverse=True)