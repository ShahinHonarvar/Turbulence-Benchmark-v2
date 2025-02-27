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

def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    truncatable_primes = []
    for num in range(23, x + 1):
        if all_left_truncatable_prime(num) and all_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes

def all_left_truncatable_prime(num):
    s = str(num)
    return all((is_prime(int(s[:i])) for i in range(1, len(s))))

def all_right_truncatable_prime(num):
    s = str(num)
    return all((is_prime(int(s[i:])) for i in range(len(s) - 1)))