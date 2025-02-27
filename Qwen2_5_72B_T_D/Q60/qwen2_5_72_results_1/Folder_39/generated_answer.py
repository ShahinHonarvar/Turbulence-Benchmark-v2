from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_lr_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not isprime(int(n_str[i:])) or not isprime(int(n_str[:-i])):
                return False
        return isprime(n)
    return [n for n in range(2, x + 1) if is_lr_truncatable_prime(n)][::-1]