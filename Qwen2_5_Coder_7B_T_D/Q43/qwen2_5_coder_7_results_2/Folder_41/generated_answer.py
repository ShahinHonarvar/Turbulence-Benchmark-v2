from sympy import isprime

def find_primes_between_indices(numbers):
    primes = [num for num in numbers[45:81] if isprime(num)]
    primes.sort(reverse=True)
    return primes