def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    primes = [2, 3, 5, 7]
    left_right_truncatable = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num)))) and all((is_prime(int(str_num[-i:])) for i in range(1, len(str_num)))):
            primes.extend([num] if num not in primes else [])
            primes.sort()
    return [p for p in primes if p >= 23 and p <= x]