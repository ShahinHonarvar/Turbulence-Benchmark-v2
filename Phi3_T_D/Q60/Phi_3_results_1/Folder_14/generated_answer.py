def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_primes(numbers):
    x = numbers[78]
    truncatable_primes = []
    for num in range(x, 1, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i + 1])):
                break
        else:
            truncatable_primes.append(num)
    return truncatable_primes