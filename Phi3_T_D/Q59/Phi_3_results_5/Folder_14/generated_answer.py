from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []

    def is_left_truncatable(n, base=10):
        n = str(n)
        for i in range(len(n)):
            if not isprime(int(n[i:])):
                return False
        return True
    for number in range(x - 1, 1, -1):
        if isprime(number) and is_left_truncatable(number):
            truncatable_primes.append(number)
    return truncatable_primes