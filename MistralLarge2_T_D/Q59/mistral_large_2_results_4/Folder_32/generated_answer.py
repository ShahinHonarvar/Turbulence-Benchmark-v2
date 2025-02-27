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
    x = numbers[42]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        left_truncate = str(num)
        while left_truncate:
            if not is_prime(int(left_truncate)):
                break
            left_truncate = left_truncate[1:]
        else:
            primes.append(num)
    return sorted(primes)