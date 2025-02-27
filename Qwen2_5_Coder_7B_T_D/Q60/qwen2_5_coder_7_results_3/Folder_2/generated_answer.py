def all_left_right_truncatable_prime(t):
    x = t[618]
    primes = []
    for num in range(2, x + 1):
        if str(num).count('0') == 0 and is_prime(num):
            temp = num
            while temp >= 10:
                temp = temp // 10
                if not is_prime(temp):
                    break
            temp = num
            while temp >= 10:
                temp = temp % 100
                if not is_prime(temp):
                    break
            else:
                primes.append(num)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True