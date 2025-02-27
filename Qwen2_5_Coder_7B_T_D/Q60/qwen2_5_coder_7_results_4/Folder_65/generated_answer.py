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
    x = numbers[32]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                left_truncatable = True
                right_truncatable = True
                for i in range(len(num_str)):
                    if not is_prime(int(num_str[i:])):
                        left_truncatable = False
                    if not is_prime(int(num_str[:-i - 1])):
                        right_truncatable = False
                if left_truncatable and right_truncatable:
                    primes.append(num)
    return sorted(primes)