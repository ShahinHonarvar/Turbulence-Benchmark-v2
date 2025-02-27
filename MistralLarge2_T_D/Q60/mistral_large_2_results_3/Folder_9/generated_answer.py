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

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    left = 0
    right = len(str_n) - 1
    while left < right:
        if not is_prime(int(str_n[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes