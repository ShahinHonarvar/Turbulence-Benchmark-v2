def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            s = str(num)
            left_truncatable = True
            while s:
                if not is_prime(int(s)):
                    left_truncatable = False
                    break
                s = s[1:]
            if left_truncatable:
                primes.append(num)
    return sorted(primes)