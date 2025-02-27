from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n) or '0' in str(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers[78]
    result = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(result, reverse=True)