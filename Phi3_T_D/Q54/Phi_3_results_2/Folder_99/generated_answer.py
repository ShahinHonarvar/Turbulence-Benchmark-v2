def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(number_tuple):
    x = number_tuple[758]
    right_truncatable_primes = []
    for num in range(2, x):
        string_num = str(num)
        for i in range(len(string_num)):
            if not is_prime(int(string_num[i:])):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)