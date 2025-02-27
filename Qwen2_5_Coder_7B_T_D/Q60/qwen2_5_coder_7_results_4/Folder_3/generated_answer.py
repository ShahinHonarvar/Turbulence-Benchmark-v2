from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    left_right_truncatable_primes = []

    def is_left_right_truncatable(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not isprime(int(num_str[i:])) or not isprime(int(num_str[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num) and is_left_right_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)