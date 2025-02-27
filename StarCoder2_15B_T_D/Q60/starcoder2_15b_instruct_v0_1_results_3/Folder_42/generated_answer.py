def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[64]
    truncatable_primes = []
    for i in range(2, x + 1):
        if isprime(i):
            num = i
            while num > 9:
                num = int(str(num)[1:])
                if not isprime(num):
                    break
            else:
                num = i
                while num > 9:
                    num = int(str(num)[:-1])
                    if not isprime(num):
                        break
                else:
                    truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes