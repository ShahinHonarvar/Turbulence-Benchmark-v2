def is_right_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 14:
        raise ValueError('Tuple must have at least 15 elements, with the 14th being the upper limit for search.')
    upper_limit = numbers[14]
    if upper_limit < 11:
        return []
    primes = {2, 3, 5, 7}
    for num in range(11, upper_limit + 1):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            is_truncatable_right = True
            str_num = str(num)
            for i in range(len(str_num)):
                if not is_right_truncatable_prime(int(str_num[i:]), primes):
                    is_truncatable_right = False
                    break
            str_num_reversed = str_num[::-1]
            is_truncatable_left = True
            for i in range(1, len(str_num_reversed)):
                if not is_right_truncatable_prime(int(str_num_reversed[:i]), primes):
                    is_truncatable_left = False
                    break
            if is_truncatable_right and is_truncatable_left:
                primes.add(num)
    return sorted(primes)