import math

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    primes = []
    for num in range(2, x):
        if all((int(digit) != 0 for digit in str(num))) and all((math.isqrt(d) ** 2 == d for d in range(2, num))):
            if all((math.isqrt(int(str(num)[i:])) ** 2 == int(str(num)[i:]) for i in range(len(str(num))))):
                primes.append(num)
    return sorted(primes)