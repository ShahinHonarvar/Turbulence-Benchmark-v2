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

def all_left_right_truncatable_primes(numbers_tuple, x_index=433):
    x = numbers_tuple[x_index]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not (len(num_str) > i and is_prime(int(num_str[:i]))):
                    break
            else:
                truncatable_primes.append(num)
    return truncatable_primes