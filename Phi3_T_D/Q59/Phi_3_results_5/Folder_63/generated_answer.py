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

def left_truncatable_primes(n):
    primes = []
    for num in range(7, n):
        if num < 10:
            primes.append(num)
            continue
        num_str = str(num)
        if all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
            primes.append(num)
    return primes

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    return left_truncatable_primes(x)