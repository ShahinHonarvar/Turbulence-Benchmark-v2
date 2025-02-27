def all_left_truncatable_prime(input_tuple):
    x = input_tuple[466]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num in [2, 3, 5, 7]:
            return True
        if any((num % d == 0 for d in range(2, int(num ** 0.5) + 1))):
            return False
        for i in range(1, len(str(num))):
            if int(str(num)[i:]) % 2 == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)