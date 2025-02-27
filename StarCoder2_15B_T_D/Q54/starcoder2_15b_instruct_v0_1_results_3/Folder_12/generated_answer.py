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
    x = numbers[70]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            truncated_num = i
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    break
                truncated_num //= 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)