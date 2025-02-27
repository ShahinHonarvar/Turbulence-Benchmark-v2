def all_left_truncatable_prime(numbers):
    x = numbers[77]

    def is_left_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for d in str(n):
            if d == '0':
                return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return sorted([n for n in range(x) if is_left_truncatable_prime(n)], reverse=True)