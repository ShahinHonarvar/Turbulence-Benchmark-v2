def all_left_right_truncatable_prime(tup):
    x = tup[30]

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True