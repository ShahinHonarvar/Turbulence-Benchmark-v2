def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = [2, 3, 5, 7]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(11, x + 1, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        if all((is_prime(int(str_num[:i])) for i in range(1, len(str_num)))):
            if all((is_prime(int(str_num[-i:])) for i in range(1, len(str_num)))):
                result.append(num)
                primes.extend([int(str_num[:i]) for i in range(1, len(str_num)) if int(str_num[:i]) not in primes])
                primes.extend(([int(str_num[-i:])] for i in range(1, len(str_num)) if int(str_num[-i:]) not in primes))
    result.sort()
    return result