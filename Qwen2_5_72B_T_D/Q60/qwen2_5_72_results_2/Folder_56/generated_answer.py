from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not isprime(int(str(n)[i:])):
                return False
            if not isprime(int(str(n)[:-i])):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result