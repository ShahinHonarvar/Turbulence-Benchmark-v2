from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[177]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            temp_num = num
            is_right_truncatable = True
            while temp_num > 0:
                if not isprime(temp_num):
                    is_right_truncatable = False
                    break
                temp_num //= 10
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)