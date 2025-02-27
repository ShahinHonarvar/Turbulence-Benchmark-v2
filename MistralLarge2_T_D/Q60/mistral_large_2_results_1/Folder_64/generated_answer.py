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

def all_left_right_truncatable_prime(t):
    x = t[4]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and '0' not in str(num):
            left_right_truncatable = True
            temp = str(num)
            while len(temp) > 1:
                if not is_prime(int(temp)):
                    left_right_truncatable = False
                    break
                temp = temp[1:-1]
            if left_right_truncatable:
                primes.append(num)
    return sorted(primes)