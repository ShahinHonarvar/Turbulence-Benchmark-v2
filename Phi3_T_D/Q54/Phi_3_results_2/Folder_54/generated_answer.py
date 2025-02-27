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

def all_right_truncatable_prime(int_tuple):
    x = int_tuple[88]
    truncatable_primes = []
    for num in range(x - 1, 1, -1):
        if not is_prime(num):
            continue
        num_str = str(num)
        is_truncatable_prime = True
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(num)
    return truncatable_primes