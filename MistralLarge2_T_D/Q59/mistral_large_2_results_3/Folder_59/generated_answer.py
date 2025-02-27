def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[84]

    def is_left_truncatable_prime(num):
        s = str(num)
        while s:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
        return True
    lt_primes = [num for num in range(2, x) if is_left_truncatable_prime(num)]
    return sorted(lt_primes, reverse=True)