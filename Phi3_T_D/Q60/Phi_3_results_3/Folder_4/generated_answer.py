def is_truncatable_prime(num):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(len(str(num))):
        if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:len(str(num)) - i])):
            return False
    return True

def all_left_right_truncatable_prime(range_tuple):
    x = range_tuple[96]
    return sorted([p for p in range(2, x + 1) if is_truncatable_prime(p)], reverse=True)