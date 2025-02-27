def all_left_right_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = nums[70]
    truncatable_primes = set()
    for num in range(2, x + 1):
        if is_prime(num):
            digits = [int(d) for d in str(num)]
            is_truncatable = True
            for i in range(1, len(digits)):
                if not is_prime(int(''.join(map(str, digits[i:])))) or not is_prime(int(''.join(map(str, digits[:-i])))):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)