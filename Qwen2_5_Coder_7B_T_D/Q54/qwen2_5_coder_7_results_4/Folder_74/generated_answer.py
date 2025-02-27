def all_right_truncatable_prime(numbers):
    x = numbers[36]
    primes = [2, 3, 5, 7]
    right_truncatable_primes = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(11, x):
        if is_prime(num):
            str_num = str(num)
            if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num)))):
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)