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
    x = numbers[54]
    primes = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            s = str(i)
            truncatable = True
            for j in range(1, len(s)):
                if not is_prime(int(s[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes)