def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    num_str = str(num)
    if len(num_str) <= 2:
        return True
    return is_truncatable_prime(int(num_str[1:])) and is_truncatable_prime(int(num_str[:-1]))

def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)