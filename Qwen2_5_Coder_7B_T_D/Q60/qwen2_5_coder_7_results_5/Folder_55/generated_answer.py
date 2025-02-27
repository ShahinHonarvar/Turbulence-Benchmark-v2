from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[73]

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num = n
        while num >= 10:
            num = int(str(num)[1:])
            if not isprime(num):
                return False
        num = n
        while num >= 10:
            num = int(str(num)[:-1])
            if not isprime(num):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable(n) and isprime(n)], reverse=True)