def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    primes = [2, 3, 5, 7]
    left_right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(8, x + 1, 2):
        if '0' not in str(i) and is_prime(i):
            str_i = str(i)
            is_lr_truncatable = True
            for j in range(len(str_i)):
                if not is_prime(int(str_i[j:])) or not is_prime(int(str_i[:len(str_i) - j])):
                    is_lr_truncatable = False
                    break
            if is_lr_truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)