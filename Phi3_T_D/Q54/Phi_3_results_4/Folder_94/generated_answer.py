def all_right_truncatable_prime(nums):

    def is_right_truncatable_prime(num, truncs):
        if num in truncs:
            return True
        if not all((num % d for d in range(2, int(num ** 0.5) + 1))):
            return False
        if len(str(num)) > 1:
            return is_right_truncatable_prime(num // 10, truncs | {num})
        return True
    try:
        limit = nums[43]
    except IndexError:
        return []
    primes = [2, 3, 5, 7]
    truncs = set(primes)
    num = 11
    while num <= limit:
        if is_right_truncatable_prime(num, truncs):
            truncs.add(num)
        num += 2
    return sorted(list(truncs))