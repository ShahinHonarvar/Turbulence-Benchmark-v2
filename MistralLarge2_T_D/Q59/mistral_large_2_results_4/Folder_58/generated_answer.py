def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[975]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        temp = num
        is_truncatable = True
        while temp > 0:
            if not is_prime(temp):
                is_truncatable = False
                break
            temp = int(str(temp)[1:])
        if is_truncatable:
            primes.append(num)
    primes.sort(reverse=True)
    return primes