def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[22]
    lr_truncatable_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_right_truncatable = True
        for i in range(len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                left_right_truncatable = False
                break
        if left_right_truncatable:
            lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)