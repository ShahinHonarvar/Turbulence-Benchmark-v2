from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[70]
    result = []

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not isprime(int(str_n[i:])):
                return False
            if not isprime(int(str_n[:len(str_n) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)