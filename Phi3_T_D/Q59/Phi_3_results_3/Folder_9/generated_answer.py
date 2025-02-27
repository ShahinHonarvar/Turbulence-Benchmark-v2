def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = [s for s in map(str, range(2, x)) if s != '0']
    output = []
    for prime in primes:
        num = int(prime)
        if all((is_prime(int(prime[i:])) for i in range(len(prime)))):
            output.append(num)
    return sorted(output, reverse=True)