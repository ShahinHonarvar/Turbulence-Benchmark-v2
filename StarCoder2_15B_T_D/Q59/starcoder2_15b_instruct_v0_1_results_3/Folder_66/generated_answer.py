def all_left_truncatable_prime(args):
    x = args[25]
    left_truncatable_primes = []
    for num in range(2, x):
        is_left_truncatable = True
        temp = num
        while temp > 0:
            if not is_prime(temp) or str(temp).startswith('0'):
                is_left_truncatable = False
                break
            temp = int(str(temp)[1:])
        if is_left_truncatable:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True