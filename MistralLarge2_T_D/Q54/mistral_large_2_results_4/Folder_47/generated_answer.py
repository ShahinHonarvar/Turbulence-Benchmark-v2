def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[49]

    def is_right_truncatable_prime(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    return sorted(result)