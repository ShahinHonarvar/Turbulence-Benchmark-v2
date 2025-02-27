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
    x = numbers[803]
    primes = [2, 3, 5, 7]
    for num in range(10, x + 1):
        if '0' not in str(num) and all((is_prime(int(str(num)[:i])) and is_prime(int(str(num)[-i:])) for i in range(1, len(str(num)) + 1))):
            primes.append(num)
    return sorted(primes)