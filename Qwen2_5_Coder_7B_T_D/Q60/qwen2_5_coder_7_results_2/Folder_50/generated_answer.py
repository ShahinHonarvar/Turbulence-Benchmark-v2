from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    left_right_primes = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        while num_str:
            if not isprime(int(num_str)):
                return False
            num_str = num_str[1:]
            if not num_str:
                break
            num_str = num_str[:-1]
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            left_right_primes.append(num)
    return sorted(left_right_primes, reverse=True)