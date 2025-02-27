from sympy import primerange

def all_left_truncatable_prime(numbers):
    n = max(numbers[-1], 10)
    primes_set = set(primerange(2, n))

    def is_left_truncatable_prime(number):
        while number in primes_set:
            number = number % (10 ** len(str(number)) // 10)
            if number == 0:
                return False
        return True
    return [p for p in primes_set if all((is_left_truncatable_prime(p // 10 ** i) for i in range(len(str(p)))))]