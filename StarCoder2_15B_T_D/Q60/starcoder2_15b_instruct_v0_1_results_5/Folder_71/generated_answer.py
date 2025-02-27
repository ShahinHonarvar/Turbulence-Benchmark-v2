def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            for j in range(i + 1, len(num_str)):
                if not is_prime(int(num_str[i:j])):
                    return False
        return is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[22]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)