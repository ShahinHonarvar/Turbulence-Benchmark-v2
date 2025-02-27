def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if '0' in str(n) or not is_prime(n):
        return False
    for i in range(len(str(n))):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[0:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[94]
    prime_list = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return prime_list