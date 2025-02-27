def all_left_right_truncatable_prime(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = n[70]
    lr_trunc_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        valid = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                valid = False
                break
        if valid:
            lr_trunc_primes.append(num)
    return lr_trunc_primes