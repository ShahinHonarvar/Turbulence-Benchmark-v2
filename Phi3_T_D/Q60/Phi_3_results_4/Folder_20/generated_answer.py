def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):

        def is_prime(k):
            if k < 2:
                return False
            for i in range(2, int(k ** 0.5) + 1):
                if k % i == 0:
                    return False
            return True
        str_n = str(n)
        for length in range(1, len(str_n)):
            if not (is_prime(int(str_n[length:])) and is_prime(int(str_n[:length]))):
                return False
        return is_prime(n)
    x = numbers[100]
    return sorted([i for i in range(10, x + 1) if is_truncatable_prime(i)], reverse=True)