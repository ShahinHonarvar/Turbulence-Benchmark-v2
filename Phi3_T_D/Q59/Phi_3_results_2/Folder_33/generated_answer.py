def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums, index=945):
    x = nums[index]

    def is_left_truncatable(number):
        if not str(number).startswith('0'):
            for i in range(len(str(number))):
                if not is_prime(int(str(number)[i:])):
                    return False
            return True
        return False
    return sorted([prime for prime in range(x, 1, -1) if is_prime(prime) and is_left_truncatable(prime)], reverse=True)