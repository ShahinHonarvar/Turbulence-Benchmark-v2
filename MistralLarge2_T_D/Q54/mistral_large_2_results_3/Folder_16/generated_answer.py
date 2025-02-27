def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[792]
    primes = []
    for num in range(2, x):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            primes.append(num)
    return sorted(primes)