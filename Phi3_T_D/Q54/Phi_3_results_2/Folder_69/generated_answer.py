def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    temp = n
    while temp > 0:
        if not is_prime(temp):
            return False
        temp //= 10
    return True

def get_primes_from_string(s):
    return [int(s[i:]) for i in range(len(s)) if is_prime(int(s[i:]))]

def all_right_truncatable_prime(numbers):
    if len(numbers) < 760:
        return []
    x = numbers[759]
    if x < 11:
        return []
    primes = [2, 3, 5, 7]
    temp = 10
    while temp < x:
        new_primes = get_primes_from_string(str(temp))
        if not new_primes:
            break
        primes.extend(new_primes)
        temp *= 10
    right_truncatables = sorted(list(set(primes) & set(get_primes_from_string(str(x)))), reverse=True)
    return right_truncatables