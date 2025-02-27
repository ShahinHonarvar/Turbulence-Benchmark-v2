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

def is_left_and_right_truncatable(number, primes):
    str_num = str(number)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
            return False
    return True if len(str_num) > 1 else is_prime(number)

def all_left_and_right_truncatable_prime(numbers):
    x = numbers[14] if len(numbers) > 14 else 2
    result = []
    primes_cache = [i for i in range(x + 1) if is_prime(i)]
    for prime in reversed(primes_cache):
        if is_left_and_right_truncatable(prime, primes_cache):
            result.append(prime)
    return result