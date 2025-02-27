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

def is_left_right_truncatable_prime(n):
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[10]
    primes_list = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(primes_list, reverse=True)