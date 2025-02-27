def all_right_truncatable_prime(t):
    x = t[26]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x):
        if is_prime(num):
            str_num = str(num)
            while str_num:
                if not is_prime(int(str_num)):
                    break
                str_num = str_num[:-1]
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)