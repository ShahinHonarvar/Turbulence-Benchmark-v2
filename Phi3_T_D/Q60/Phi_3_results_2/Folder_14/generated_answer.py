def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

def all_left_right_truncatable_prime(nums):
    x = nums[78]
    valid_primes = []
    primes_set = set()
    for num in range(23, x + 1):
        str_num = str(num)
        num_length = len(str_num)
        current = num
        is_truncatable = True
        for i in range(num_length):
            if is_prime(current):
                primes_set.add(current)
            if not is_prime(current) or current not in primes_set:
                is_truncatable = False
                break
            current = int(str_num[i:num_length])
        current = num
        for i in range(num_length):
            if not is_prime(current) or current not in primes_set:
                is_truncatable = False
                break
            current = int(str_num[:i + 1])
        if is_truncatable:
            valid_primes.append(num)
    return sorted(valid_primes, reverse=True)