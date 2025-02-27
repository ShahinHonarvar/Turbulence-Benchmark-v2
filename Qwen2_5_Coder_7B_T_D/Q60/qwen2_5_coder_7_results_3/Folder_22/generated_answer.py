def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[85]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        if all((is_prime(int(num_str[:i])) for i in range(1, len(num_str)))) and all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes