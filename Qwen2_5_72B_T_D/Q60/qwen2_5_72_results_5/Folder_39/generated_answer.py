from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_truncatable_prime(num):
        s = str(num)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return isprime(int(s))
    return [p for p in range(2, x + 1) if is_truncatable_prime(p)][::-1]