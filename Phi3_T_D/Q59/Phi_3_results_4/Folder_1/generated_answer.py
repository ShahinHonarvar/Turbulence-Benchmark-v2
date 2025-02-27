def all_left_truncatable_prime(numbers):
    x = numbers[20]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    return sorted([i for i in range(23, x) if is_prime(i) and is_truncatable(i)], reverse=True)