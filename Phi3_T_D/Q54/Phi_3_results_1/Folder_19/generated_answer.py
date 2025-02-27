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
    x = numbers[67]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []
    for num in range(11, x, 2):
        s = str(num)
        right_truncated = True
        for i in range(len(s)):
            truncated = int(s[:len(s) - i])
            if not is_prime(truncated):
                right_truncated = False
                break
        if right_truncated:
            primes.append(num)
    return sorted(primes, reverse=True)