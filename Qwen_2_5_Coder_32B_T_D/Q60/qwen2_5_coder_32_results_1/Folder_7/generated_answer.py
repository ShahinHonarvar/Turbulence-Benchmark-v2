def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[803]
    truncatable_primes = []
    for num in range(11, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            all_truncatable = True
            for i in range(1, len(num_str) - 1):
                if not (is_prime(int(num_str[i:])) and is_prime(int(num_str[:-i]))):
                    all_truncatable = False
                    break
            if all_truncatable and is_prime(int(num_str[1:])) and is_prime(int(num_str[:-1])):
                truncatable_primes.append(num)
    return truncatable_primes