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

def all_right_truncatable_prime(numbers):
    x = numbers[6]
    right_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        n_str = str(n)
        for i in range(len(n_str)):
            if is_prime(int(n_str[i:])):
                right_truncatable_primes.append(n)
                break
    return right_truncatable_primes