def all_right_truncatable_prime(t):
    x = t[11]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(prime, digits):
        if is_prime(prime):
            for i in range(digits):
                prime //= 10
                if not is_prime(prime):
                    return False
        return True
    right_truncs = []
    digits = len(str(x))
    candidate = 10
    while candidate < x:
        if is_right_truncatable_prime(candidate, digits):
            right_truncs.append(candidate)
        candidate += 10
    return sorted(right_truncs)