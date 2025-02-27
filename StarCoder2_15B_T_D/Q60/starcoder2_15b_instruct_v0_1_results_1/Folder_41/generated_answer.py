def is_truncatable_prime(num: int) -> bool:
    num_str = str(num)
    for i in range(len(num_str)):
        truncated_num = int(num_str[i:])
        if not is_prime(truncated_num):
            return False
        truncated_num = int(num_str[:len(num_str) - i])
        if not is_prime(truncated_num):
            return False
    return True

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers: tuple) -> list:
    x = numbers[46]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes