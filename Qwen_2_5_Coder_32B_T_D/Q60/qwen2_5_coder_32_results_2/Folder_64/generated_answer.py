def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[4]
    truncatable_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left = num
        right = num
        is_truncatable = True
        while left > 9 and right > 9:
            if not is_prime(left) or not is_prime(right):
                is_truncatable = False
                break
            left = int(s[1:])
            right = int(s[:-1])
            s = s[1:-1]
        if is_truncatable and (is_prime(left) or len(s) == 1) and (is_prime(right) or len(s) == 1):
            truncatable_primes.append(num)
    return truncatable_primes