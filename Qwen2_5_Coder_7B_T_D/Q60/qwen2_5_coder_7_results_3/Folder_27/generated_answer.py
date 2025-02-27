from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    max_value = max(numbers)

    def is_left_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if '0' in s[i:] or not isprime(int(s[i:])):
                return False
            if '0' in s[:-i - 1] or not isprime(int(s[:-i - 1])):
                return False
        return True
    return sorted([n for n in range(2, max_value + 1) if isprime(n) and is_left_right_truncatable(n)], reverse=True)