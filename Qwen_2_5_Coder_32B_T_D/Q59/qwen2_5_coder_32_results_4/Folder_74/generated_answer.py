def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    left_truncatable_primes = []
    for num in range(2, x):
        snum = str(num)
        if '0' in snum:
            continue
        truncatable = True
        for i in range(len(snum)):
            if not is_prime(int(snum[i:])):
                truncatable = False
                break
        if truncatable:
            left_truncatable_primes.append(num)
    return left_truncatable_primes