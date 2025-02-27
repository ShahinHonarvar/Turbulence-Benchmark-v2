def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_primes(numbers):
    x = numbers[19]
    result = []
    for num in range(23, x + 1):
        num_str = str(num)
        if is_prime(num):
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                    break
            else:
                result.append(num)
    return result