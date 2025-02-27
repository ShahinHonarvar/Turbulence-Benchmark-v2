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

def is_right_truncatable_prime(n):
    n_str = str(n)
    while n_str:
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[:-1]
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[71]
    right_truncatables = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    return sorted(right_truncatables, reverse=True)