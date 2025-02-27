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

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp = num
        is_truncatable = True
        while temp > 0 and is_truncatable:
            if not is_prime(temp):
                is_truncatable = False
            temp = int(str(temp)[1:-1]) if len(str(temp)) > 1 else 0
        if is_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)