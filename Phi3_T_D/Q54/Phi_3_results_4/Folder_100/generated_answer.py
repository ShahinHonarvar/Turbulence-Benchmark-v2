def all_right_truncatable_prime(numbers):
    x = numbers[26]
    right_truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num, primes):
        str_num = str(num)
        for i in range(len(str_num)):
            if is_prime(int(str_num[:i + 1])):
                continue
            else:
                return False
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num, right_truncatable_primes):
            right_truncatable_primes.append(num)
    return sorted([p for p in right_truncatable_primes if is_prime(p)])