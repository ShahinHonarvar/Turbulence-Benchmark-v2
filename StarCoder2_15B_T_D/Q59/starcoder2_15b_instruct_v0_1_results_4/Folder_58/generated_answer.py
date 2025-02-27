def all_left_truncatable_prime(input_tuple):
    x = input_tuple[975]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        for digit in str(num):
            if digit == '0':
                return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(x):
        if is_left_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result