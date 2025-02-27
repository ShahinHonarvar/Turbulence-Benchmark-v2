from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    left_right_trunc_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            num_str = str(num)
            is_lr_trunc_prime = True
            for i in range(len(num_str)):
                if not isprime(int(num_str[i:])) or not isprime(int(num_str[:len(num_str) - i])):
                    is_lr_trunc_prime = False
                    break
            if is_lr_trunc_prime:
                left_right_trunc_primes.append(num)
    return sorted(left_right_trunc_primes, reverse=True)