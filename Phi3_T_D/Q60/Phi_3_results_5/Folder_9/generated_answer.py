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

def is_left_right_truncatable(n):
    if not is_prime(n):
        return False
    str_num = str(n)
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    filtered_primes = [i for i in range(x, 0, -1) if is_prime(i) and is_left_right_truncatable(i)]
    return filtered_primes