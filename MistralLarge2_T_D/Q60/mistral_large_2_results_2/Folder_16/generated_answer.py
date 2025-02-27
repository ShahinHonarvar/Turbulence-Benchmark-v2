def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def all_left_right_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[792]

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 1:
            if not is_prime(int(str_num)) or not is_prime(int(str_num[::-1])):
                return False
            str_num = str_num[1:-1]
        return is_prime(int(str_num))
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes)