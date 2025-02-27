import math

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    if x < 71:
        return []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(10, x):
        is_truncatable = True
        for i in range(1, len(str(num))):
            truncated_num = int(str(num)[:-i])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)