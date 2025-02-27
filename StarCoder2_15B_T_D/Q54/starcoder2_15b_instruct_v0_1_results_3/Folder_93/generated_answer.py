def all_right_truncatable_prime(args):
    n = args[11]

    def is_right_truncatable_prime(num):
        while num >= 10:
            if not is_prime(num):
                return False
            num //= 10
        return is_prime(num)

    def is_prime(num):
        return all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
    return sorted(filter(is_right_truncatable_prime, range(2, n)))