from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[46]
    right_truncatable_primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if isprime(temp):
                temp = temp // 10
            else:
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)