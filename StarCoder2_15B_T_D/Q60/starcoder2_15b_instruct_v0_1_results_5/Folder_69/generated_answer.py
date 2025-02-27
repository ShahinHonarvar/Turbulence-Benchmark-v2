def all_left_right_truncatable_prime(values):
    x = values[760]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if not is_prime(truncated_number):
                is_truncatable_prime = False
                break
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

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