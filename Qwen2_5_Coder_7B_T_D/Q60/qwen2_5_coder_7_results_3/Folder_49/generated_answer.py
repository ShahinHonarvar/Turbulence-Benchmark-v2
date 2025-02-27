from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    truncatable_primes = []

    def is_truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)