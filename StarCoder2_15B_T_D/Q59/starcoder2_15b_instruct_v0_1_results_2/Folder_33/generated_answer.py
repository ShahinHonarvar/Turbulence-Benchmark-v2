def all_left_truncatable_prime(input_tuple):
    x = input_tuple[945]

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return is_prime(num)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)