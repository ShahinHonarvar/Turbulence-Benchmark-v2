from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_lr_truncatable_prime(n):
        if '0' in str(n) or n < 10:
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not isprime(int(str_n[i:])) or not isprime(int(str_n[:-i])):
                return False
        return True
    x = numbers[69]
    result = [num for num in range(10, x + 1) if is_lr_truncatable_prime(num)]
    return sorted(result, reverse=True)