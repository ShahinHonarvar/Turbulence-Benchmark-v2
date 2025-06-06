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
    x = numbers[37] - 1
    truncatable_primes = []
    for num in range(x, 1, -1):
        num_str = str(num)
        is_truncatable = True
        while num > 0:
            if not is_prime(int(num_str)):
                is_truncatable = False
                break
            num_str = num_str[:-1]
        if is_truncatable:
            truncatable_primes.append(num)
    return truncatable_primes