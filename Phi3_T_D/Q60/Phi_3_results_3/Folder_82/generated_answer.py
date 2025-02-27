def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        return all((is_prime(int(n[i:])) and is_prime(int(n[:len(n) - i])) for i in range(len(n))))
    x = int(numbers[69])
    return sorted([p for p in range(2, x + 1) if is_truncatable_prime(p)], reverse=True)