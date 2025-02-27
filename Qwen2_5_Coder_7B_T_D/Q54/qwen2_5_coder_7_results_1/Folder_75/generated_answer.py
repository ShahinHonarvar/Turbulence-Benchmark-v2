def all_right_truncatable_prime(lst):
    x = lst[41]
    right_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x):
        str_num = str(num)
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)