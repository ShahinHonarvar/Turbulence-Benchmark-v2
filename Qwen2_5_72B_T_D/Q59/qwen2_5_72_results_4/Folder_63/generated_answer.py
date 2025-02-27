from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[88]

    def is_left_truncatable_prime(n):
        if not isprime(n):
            return False
        number_str = str(n)
        if '0' in number_str:
            return False
        for i in range(1, len(number_str)):
            if not isprime(int(number_str[i:])):
                return False
        return True
    result = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(result)