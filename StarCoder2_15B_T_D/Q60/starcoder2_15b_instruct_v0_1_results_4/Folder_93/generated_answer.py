def all_left_right_truncatable_prime(tuple_of_positive_integers):
    left_right_truncatable_primes = []
    for num in tuple_of_positive_integers:
        if num > 10 and is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)

def is_left_right_truncatable_prime(num):
    num_str = str(num)
    if len(num_str) <= 2:
        return is_prime(num)
    if num_str.startswith('0') or num_str.endswith('0'):
        return False
    return is_prime(num) and is_left_right_truncatable_prime(int(num_str[1:])) and is_left_right_truncatable_prime(int(num_str[:-1]))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True