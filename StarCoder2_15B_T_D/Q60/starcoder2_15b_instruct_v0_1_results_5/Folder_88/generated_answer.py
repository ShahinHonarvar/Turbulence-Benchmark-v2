def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(len(num_str) - 1):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[93]
    return sorted(filter(is_truncatable_prime, range(2, x + 1)))