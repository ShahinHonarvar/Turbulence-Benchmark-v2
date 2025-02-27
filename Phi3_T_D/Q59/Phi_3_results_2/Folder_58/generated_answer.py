def all_left_truncatable_prime(int_tup):
    n = int_tup[975]

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_left_truncatable_prime(number):
        number = str(number)
        for i in range(len(number)):
            if not is_prime(int(number[i:])):
                return False
        return True
    return sorted(filter(lambda x: is_left_truncatable_prime(x), range(2, n)), reverse=True)