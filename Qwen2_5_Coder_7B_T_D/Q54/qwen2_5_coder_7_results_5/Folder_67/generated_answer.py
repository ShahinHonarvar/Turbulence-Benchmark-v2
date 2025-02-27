from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            is_right_truncatable = True
            temp_num = num
            while temp_num > 0:
                if not isprime(temp_num):
                    is_right_truncatable = False
                    break
                temp_num //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)