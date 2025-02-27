def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[20]
    primes = []
    for num in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(num))):
            truncated = int(str(num)[i:])
            if not is_prime(truncated):
                is_left_truncatable = False
                break
        if is_left_truncatable and '0' not in str(num):
            primes.append(num)
    return sorted(primes, reverse=True)