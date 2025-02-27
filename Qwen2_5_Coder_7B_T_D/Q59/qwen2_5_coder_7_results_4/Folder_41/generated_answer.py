from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = []
    for num in range(2, x):
        if isprime(num) and '0' not in str(num):
            temp = num
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)