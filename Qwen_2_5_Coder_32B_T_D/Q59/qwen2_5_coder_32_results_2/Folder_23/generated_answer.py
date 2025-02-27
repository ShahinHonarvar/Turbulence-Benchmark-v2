def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(len(n_str)):
            if not is_prime(int(n_str[i:])):
                return False
        return True
    x = numbers[77]
    result = [n for n in range(2, x) if is_left_truncatable(n)]
    return sorted(result, reverse=True)