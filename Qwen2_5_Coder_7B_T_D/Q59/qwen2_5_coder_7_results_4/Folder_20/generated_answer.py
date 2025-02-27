def all_left_truncatable_prime(numbers):
    x = numbers[100]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((int(d) != 0 for d in str(num))) and all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True