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

def all_left_right_truncatable_prime(numbers):
    x = numbers[94] if len(numbers) > 94 else 0
    left_primes = set(get_left_truncatable(x))
    right_primes = set(get_right_truncatable(x))
    return sorted(list(left_primes.intersection(right_primes)))

def get_left_truncatable(n):
    truncatable_primes = []
    for i in range(11, n + 1, 2):
        str_i = str(i)
        if is_prime(i):
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[j:])):
                    break
            else:
                if len(str_i) > 1 and '0' not in str_i:
                    truncatable_primes.append(i)
    return truncatable_primes

def get_right_truncatable(n):
    truncatable_primes = []
    for i in range(13, n + 1, 2):
        str_i = str(i)
        if is_prime(i):
            for j in range(1, len(str_i)):
                if not is_prime(int(str_i[:-j])):
                    break
            else:
                if '0' not in str_i:
                    truncatable_primes.append(i)
    return truncatable_primes