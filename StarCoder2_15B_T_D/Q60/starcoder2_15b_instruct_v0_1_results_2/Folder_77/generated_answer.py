def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    left_right_truncatable_primes = []
    for num in range(10, x + 1):
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True