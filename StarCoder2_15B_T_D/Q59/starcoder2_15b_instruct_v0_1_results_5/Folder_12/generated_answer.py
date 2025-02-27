def all_left_truncatable_prime(input_tuple):
    x = input_tuple[70]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)], reverse=True)

def is_left_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    return is_prime(num) and is_left_truncatable_prime(int(str(num)[1:]))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True