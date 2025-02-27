from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        if not isprime(num) or '0' in str(num):
            return False
        s = str(num)
        while len(s) > 1:
            s = s[1:-1]
            if not isprime(int(s)) or '0' in s:
                return False
        return True
    x = numbers[14]
    return sorted([num for num in range(2, x + 1) if is_truncatable_prime(num)])