from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []

    def is_right_truncatable(n):
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[:-1]
        return True
    for number in range(2, x):
        if is_right_truncatable(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)