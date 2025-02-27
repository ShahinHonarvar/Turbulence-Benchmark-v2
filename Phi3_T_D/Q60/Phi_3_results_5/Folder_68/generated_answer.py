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
    x = numbers[1]
    right_truncatable_primes = set()
    left_truncatable_primes = set()
    for i in range(7, x + 1, 2):
        if is_prime(i):
            str_i = str(i)
            right_truncatable = True
            left_truncatable = True
            for j in range(1, len(str_i) // 2 + 1):
                if int(str_i[j:]) not in right_truncatable_primes:
                    right_truncatable = False
                    break
                if int(str_i[:-j]) not in left_truncatable_primes:
                    left_truncatable = False
                    break
            if right_truncatable and left_truncatable:
                right_truncatable_primes.add(i)
                left_truncatable_primes.add(i)
    return sorted(list(right_truncatable_primes), reverse=True)