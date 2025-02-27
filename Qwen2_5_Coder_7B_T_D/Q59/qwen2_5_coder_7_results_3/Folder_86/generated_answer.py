def all_left_truncatable_prime(numbers):
    x = numbers[126]
    primes = set()
    for num in range(2, x):
        if all((int(digit) != 0 and is_prime(int(digit)) for digit in str(num))):
            primes.add(num)
    left_truncatable = []
    for prime in primes:
        is_lt_prime = True
        for i in range(len(str(prime))):
            if not is_prime(int(str(prime)[i:])):
                is_lt_prime = False
                break
        if is_lt_prime:
            left_truncatable.append(prime)
    return sorted(left_truncatable, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True