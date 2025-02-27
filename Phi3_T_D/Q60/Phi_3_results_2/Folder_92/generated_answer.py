def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_left_right_truncatable_prime(numbers):
    if not 2 <= numbers[7] < 10:
        return []
    truncatable_primes = []
    for num in range(23, min(numbers[7] + 1, 1000)):
        if is_prime(num):
            is_truncatable = True
            str_num = str(num)
            for i in range(1, len(str_num)):
                if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return truncatable_primes