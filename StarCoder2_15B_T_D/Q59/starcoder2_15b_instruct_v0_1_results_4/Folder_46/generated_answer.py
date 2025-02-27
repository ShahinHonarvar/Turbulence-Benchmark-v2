def is_left_truncatable_prime(num):
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[33]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes