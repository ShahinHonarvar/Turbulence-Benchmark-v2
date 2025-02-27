from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not (isprime(int(str_n[i:])) and isprime(int(str_n[:-i]))):
                return False
        return True
    return [n for n in range(2, x + 1) if is_truncatable_prime(n)][::-1]