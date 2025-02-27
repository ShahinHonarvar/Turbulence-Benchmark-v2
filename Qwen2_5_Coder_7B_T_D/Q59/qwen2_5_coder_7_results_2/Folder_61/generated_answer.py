from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    primes = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        flag = True
        for i in range(len(str(prime))):
            if not isprime(int(str(prime)[i:])):
                flag = False
                break
        if flag:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)