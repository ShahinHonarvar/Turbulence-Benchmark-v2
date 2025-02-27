from sympy import primerange

def all_right_truncatable_prime(numbers):
    x = numbers[26]
    right_truncatable_primes = []
    for num in primerange(2, x):
        num_str = str(num)
        is_right_truncatable = True
        for i in range(len(num_str)):
            if int(num_str[i:]) not in primerange(2, x):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)