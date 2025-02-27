def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[630]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            tested, digit = (str(num), 0)
            while len(tested) > 1:
                digit = int(tested[0])
                if not is_prime(int(tested[1:])):
                    break
                tested = tested[1:]
            if not tested or int(tested) not in primes:
                primes.append(num)
    return primes