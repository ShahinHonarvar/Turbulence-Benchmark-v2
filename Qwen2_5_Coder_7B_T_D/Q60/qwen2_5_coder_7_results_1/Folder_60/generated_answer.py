def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:len(s) - i])):
                return False
        return True
    x = tup[87]
    result = [i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable(i)]
    return sorted(result)