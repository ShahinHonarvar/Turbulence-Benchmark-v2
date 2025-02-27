def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[96]

    def is_left_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        if '0' in str(num):
            return False
        num_str = str(num)
        while len(num_str) > 1:
            num_str = num_str[1:-1]
            if not num_str or not is_prime(int(num_str)):
                return False
        return True
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)