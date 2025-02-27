from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    x = numbers[73] if len(numbers) > 73 else 0
    primes = [i for i in range(2, x + 1) if isprime(i) and is_left_right_truncatable_prime(i)]
    return sorted(primes, reverse=True)