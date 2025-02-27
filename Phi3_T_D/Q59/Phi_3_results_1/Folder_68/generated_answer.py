def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    while n > 0:
        if not sieve[n]:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[1]
    sieve = [True] * (x + 1)
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x + 1, i):
                sieve[j] = False
    result = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_left_truncatable_prime(num, sieve):
            result.append(num)
    return result