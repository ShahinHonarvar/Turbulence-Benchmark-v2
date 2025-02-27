def all_left_truncatable_prime(numbers):
    x = numbers[645]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(10, x):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num) + 1))):
            primes.append(num)
    return sorted(primes)