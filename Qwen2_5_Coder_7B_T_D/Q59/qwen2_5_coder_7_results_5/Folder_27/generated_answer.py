from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[79]
    primes = [2, 3, 5, 7]
    for num in range(11, x):
        if all((isprime(int(str(num)[:i])) for i in range(1, len(str(num))))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes, reverse=True)