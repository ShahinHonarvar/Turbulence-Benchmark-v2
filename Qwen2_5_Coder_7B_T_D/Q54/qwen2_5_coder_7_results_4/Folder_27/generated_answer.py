from sympy import isprime

def all_right_truncatable_prime(lst):
    x = lst[79]
    right_truncatable_primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if not isprime(temp):
                break
            temp //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)