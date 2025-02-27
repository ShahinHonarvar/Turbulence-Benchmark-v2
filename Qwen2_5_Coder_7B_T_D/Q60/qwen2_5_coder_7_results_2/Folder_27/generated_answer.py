from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]
    left_right_truncatable = []
    primes = set()
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            primes.add(num)
    for prime in primes:
        left = str(prime)
        right = str(prime)
        while left and right:
            if not (isprime(int(left)) and isprime(int(right))):
                break
            left = left[1:]
            right = right[:-1]
        else:
            left_right_truncatable.append(prime)
    return sorted(left_right_truncatable, reverse=True)