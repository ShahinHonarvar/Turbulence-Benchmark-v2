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

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[784]
    right_truncatable_primes = []
    for num in range(2, x):
        if not is_prime(num):
            continue
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)