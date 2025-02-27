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
    x = numbers[67]
    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = num
        while temp > 0 and is_prime(temp):
            temp = int(str(temp)[1:])
        if temp == 0:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)