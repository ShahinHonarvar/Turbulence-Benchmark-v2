from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            num_str = str(num)
            is_left_truncatable = True
            for i in range(len(num_str)):
                if not isprime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(num)
    return sorted(primes)