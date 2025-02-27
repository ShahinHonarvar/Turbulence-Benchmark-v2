from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[57]
    right_truncatable_primes = []
    for num in range(2, x):
        if isprime(num):
            temp = num
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes