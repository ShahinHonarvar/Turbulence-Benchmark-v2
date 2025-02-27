from sympy import isprime

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    left_right_truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return left_right_truncatable_primes