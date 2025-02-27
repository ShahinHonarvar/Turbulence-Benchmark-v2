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

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    num_str = str(n)
    if '0' in num_str:
        return False
    left, right = (num_str[0], num_str[-1])
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        left += num_str[0]
        right = num_str[-1] + right
        if not is_prime(int(left)) or not is_prime(int(right)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[784]
    primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)