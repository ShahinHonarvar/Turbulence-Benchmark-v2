def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not all((c in '123456789' for c in str(n))):
        return False
    n_str = str(n)
    while n_str:
        if not is_prime(int(n_str)):
            return False
        if len(n_str) == 1 or (len(n_str) == 2 and len(n_str) < 2) or (not is_prime(int(n_str[:-1]))):
            return False
        n_str = n_str[1:]
    return True

def all_left_right_truncatable_primes(numbers, index):
    x = numbers[index]
    result = []
    for number in range(2, x + 1):
        if is_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)