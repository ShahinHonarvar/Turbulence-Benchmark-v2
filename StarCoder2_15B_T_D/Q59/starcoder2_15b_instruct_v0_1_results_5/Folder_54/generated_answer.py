def all_left_truncatable_prime(numbers):
    x = numbers[88]
    prime_numbers = [num for num in range(2, x) if is_prime(num)]
    left_truncatable_prime_numbers = [num for num in prime_numbers if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_prime_numbers, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_truncatable_prime(num):
    if '0' in str(num):
        return False
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):
            return False
    return True