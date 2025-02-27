def all_left_right_truncatable_prime(numbers):

    def is_truncatable(num):
        num_str = str(num)
        if len(num_str) <= 2:
            return False
        for i in range(len(num_str) - 1):
            if int(num_str[i + 1:]) == 0 or int(num_str[:-i - 1]) == 0:
                return False
            if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:-i - 1])):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[36]
    truncatable_primes = [prime for prime in range(2, x + 1) if is_truncatable(prime)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes