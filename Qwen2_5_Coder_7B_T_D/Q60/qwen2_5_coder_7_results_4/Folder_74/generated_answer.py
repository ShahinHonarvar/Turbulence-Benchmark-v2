def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_right_truncatable_prime(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if is_prime(int(num_str[i:])) and is_prime(int(num_str[:len(num_str) - i])):
            continue
        else:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for i in range(2, x + 1):
        if is_prime(i) and '0' not in str(i) and left_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)