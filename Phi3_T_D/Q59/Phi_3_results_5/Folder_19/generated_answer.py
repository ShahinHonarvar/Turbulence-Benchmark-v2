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

def left_truncatable_primes(n):
    result = []
    current = 2
    while current < n:
        if is_prime(current):
            str_num = str(current)
            truncatable = True
            for i in range(len(str_num) - 1):
                if not is_prime(int(str_num[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(current)
        current += 1
    return result

def all_left_truncatable_prime(tu):
    x = tu[67]
    primes = left_truncatable_primes(x)
    primes.sort(reverse=True)
    return primes