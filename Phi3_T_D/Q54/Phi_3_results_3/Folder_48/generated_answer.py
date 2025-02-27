def all_right_truncatable_prime(numbers):
    x = numbers[835]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num), 0, -1):
                if not is_prime(int(str_num[:i])):
                    break
            else:
                truncatable_primes.append(num)
    return truncatable_primes