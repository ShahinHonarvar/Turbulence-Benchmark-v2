def all_left_right_truncatable_prime(t):
    x = t[94]
    primes = [2, 3, 5, 7]
    left_right_primes = []
    for n in range(11, x + 1):
        str_n = str(n)
        if '0' not in str_n:
            temp = True
            for i in range(len(str_n)):
                if not is_prime(int(str_n[i:])):
                    temp = False
                    break
            for i in range(len(str_n) - 1, 0, -1):
                if not is_prime(int(str_n[:i])):
                    temp = False
                    break
            if temp:
                primes.append(n)
    for p in primes:
        str_p = str(p)
        if all((is_prime(int(str_p[:i])) and is_prime(int(str_p[i:])) for i in range(1, len(str_p)))):
            left_right_primes.append(p)
    return sorted(left_right_primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True