from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[54]
    primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if not isprime(temp):
                break
            temp //= 10
        else:
            primes.append(num)
    return sorted(primes, reverse=True)