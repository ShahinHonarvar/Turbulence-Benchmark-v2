from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[89]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        is_right_truncatable = True
        for i in range(len(str_num) - 1, -1, -1):
            if not isprime(int(str_num[:i + 1])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)