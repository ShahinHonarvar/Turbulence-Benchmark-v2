def all_left_right_truncatable_prime(data):

    def is_truncatable_prime(num, is_left=True):
        num_str = str(num)
        if num < 10:
            return is_prime(num)
        if num_str[0] == '0' or num_str[-1] == '0':
            return False
        if not is_prime(num):
            return False
        if is_left:
            return is_truncatable_prime(int(num_str[1:]), is_left)
        return is_truncatable_prime(int(num_str[:-1]), is_left)

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(num ** 0.5) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True
    x = data[57]
    truncatable_primes = []
    for num in range(x + 1):
        if is_truncatable_prime(num) and is_truncatable_prime(num, is_left=False):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)