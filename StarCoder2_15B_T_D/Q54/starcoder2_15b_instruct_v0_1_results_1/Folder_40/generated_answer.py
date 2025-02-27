def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[10]

    def is_right_truncatable_prime(number):
        while number >= 10:
            if not is_prime(number):
                return False
            number //= 10
        return is_prime(number)
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)], reverse=True)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True