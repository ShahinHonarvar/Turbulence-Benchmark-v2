def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        s = str(n)
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    for num in range(11, x + 1):
        if all((digit != '0' for digit in str(num))) and is_prime(num):
            primes.append(num)
    return [p for p in primes if is_lr_truncatable(p)]