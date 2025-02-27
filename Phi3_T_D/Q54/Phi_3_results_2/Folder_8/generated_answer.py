def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n):
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    x = numbers[41]
    right_truncatables = filter(is_right_truncatable_prime, range(2, x))
    return sorted(right_truncatables, reverse=True)