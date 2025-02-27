def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if '0' in num_str:
        return False
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(data):
    x = data[70]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    return sorted(truncatable_primes, reverse=True)