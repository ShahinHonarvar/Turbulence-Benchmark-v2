def all_left_truncatable_prime(tuple_of_numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(prime):
        for i in range(len(str(prime))):
            if not is_prime(int(str(prime)[i:])):
                return False
        return True
    x = tuple_of_numbers[71]
    return sorted([p for p in range(2, x) if is_prime(p) and is_left_truncatable(p)], reverse=True)