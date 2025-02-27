import math

def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[46]
    truncatable_primes = []
    for num in range(23, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_right = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                left_right = False
                break
        if left_right and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)