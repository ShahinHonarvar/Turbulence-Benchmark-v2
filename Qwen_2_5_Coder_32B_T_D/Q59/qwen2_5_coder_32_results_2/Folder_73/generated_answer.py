def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    x = numbers[97]
    result = [n for n in range(2, x) if '0' not in str(n) and is_left_truncatable_prime(n)]
    return result