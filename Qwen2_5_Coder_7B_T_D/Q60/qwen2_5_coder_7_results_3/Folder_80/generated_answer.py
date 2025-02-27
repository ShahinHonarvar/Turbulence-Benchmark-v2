from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if isprime(num):
            is_truncatable = True
            for i in range(len(num_str)):
                if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str) - i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)