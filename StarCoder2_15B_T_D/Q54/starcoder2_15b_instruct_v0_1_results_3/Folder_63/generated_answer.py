def all_right_truncatable_prime(x):

    def is_right_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))
    result = []
    for num in range(1, x[88]):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)