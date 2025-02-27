def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable = True
        for i in range(1, len(num_str) - 1):
            if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i]))):
                truncatable = False
                break
        if truncatable and is_prime(num) and is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1])):
            result.append(num)
    return result