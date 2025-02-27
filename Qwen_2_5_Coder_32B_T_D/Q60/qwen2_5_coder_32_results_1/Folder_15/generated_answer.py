def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    if x < 23:
        return []
    lr_truncatable_primes = []
    for num in range(23, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            all_truncations_prime = True
            for i in range(1, len(num_str) - 1):
                if not is_prime(int(num_str[i:-i])) or not is_prime(int(num_str[i:])):
                    all_truncations_prime = False
                    break
            if is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1])) and all_truncations_prime:
                lr_truncatable_primes.append(num)
    return sorted(lr_truncatable_primes, reverse=True)