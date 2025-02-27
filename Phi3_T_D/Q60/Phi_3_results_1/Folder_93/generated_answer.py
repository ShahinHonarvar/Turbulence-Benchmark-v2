def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(prime):
        if not all((c in '12357' for c in str(prime))):
            return False
        for length in range(1, len(str(prime))):
            if not is_prime(int(str(prime)[length:])) or not is_prime(int(str(prime)[:-length])):
                return False
        return True
    x = numbers[11]
    return sorted([p for p in range(2, x + 1) if is_prime(p) and is_truncatable_prime(p)])