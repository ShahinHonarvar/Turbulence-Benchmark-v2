from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[57]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        while len(num_str) > 1:
            if not isprime(int(num_str)) or not isprime(int(num_str[:-1])):
                return False
            num_str = num_str[1:-1]
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)