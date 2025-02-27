def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[370] if 370 < len(numbers) else 0
    truncatable_primes = []
    valid_digits = set('13572')

    def is_truncatable(number):
        s = str(number)
        for i in range(1, len(s)):
            if s[i:] not in truncatable_primes_set and (not is_prime(int(s[i:]))):
                return False
            if s[:-i] not in truncatable_primes_set and (not is_prime(int(s[:-i]))):
                return False
        return True
    truncatable_primes_set = set()
    for num in range(23, x + 1):
        if is_prime(num):
            for i in range(len(str(num))):
                if str(num)[i:] not in truncatable_primes_set and all((d in valid_digits for d in str(num)[i:])):
                    truncatable_primes_set.add(num)
                    truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)