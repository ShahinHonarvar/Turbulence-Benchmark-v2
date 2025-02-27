from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[39]

    def is_left_truncatable(number):
        str_num = str(number)
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])):
                return False
        return isprime(number)
    return sorted([n for n in range(2, x) if is_left_truncatable(n)])