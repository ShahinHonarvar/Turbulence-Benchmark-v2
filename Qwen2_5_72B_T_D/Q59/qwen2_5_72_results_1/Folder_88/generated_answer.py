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

def all_left_truncatable_prime(numbers):
    x = numbers[93]
    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)