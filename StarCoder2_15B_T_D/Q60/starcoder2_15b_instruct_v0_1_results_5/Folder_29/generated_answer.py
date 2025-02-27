def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[55]

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if len(num_str) <= 2:
            return False
        if not is_prime(num):
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:i + 1])):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes