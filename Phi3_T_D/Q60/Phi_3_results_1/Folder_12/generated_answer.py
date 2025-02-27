def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, left_to_right=True):
        if not is_prime(n):
            return False
        if left_to_right:
            if len(str(n)) == 1:
                return True
            return is_truncatable(int(str(n)[1:]), False) and is_truncatable(int(str(n)[:-1]), False)
        else:
            if len(str(n)) == 1 or (len(str(n)) == 2 and is_prime(int(str(n)[:-1]))):
                return True
            return is_truncatable(int(str(n)[1:]), True)
    x = max(numbers)
    return sorted([i for i in range(2, x + 1) if is_truncatable(i)], reverse=True)