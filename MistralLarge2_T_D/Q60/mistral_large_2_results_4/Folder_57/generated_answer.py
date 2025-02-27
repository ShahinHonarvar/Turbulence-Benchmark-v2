def all_left_right_truncatable_prime(numbers):
    x = numbers[54]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            if not is_prime(int(n_str[1:-1])):
                return False
            n_str = n_str[1:-1]
        return True
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)