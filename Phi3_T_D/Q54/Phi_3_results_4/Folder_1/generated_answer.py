def all_right_truncatable_prime(numbers):
    x = numbers[20]
    right_truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num, primes_list):
        if num < 10:
            return False
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:i])):
                return False
        return True
    for i in range(x - 1, 1, -1):
        if is_prime(i) and is_right_truncatable_prime(i, right_truncatable_primes):
            right_truncatable_primes.append(i)
    return right_truncatable_primes