def find_primes_between_indices(nums: list) -> list:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted([x for x in nums[57:64 + 1] if is_prime(x)], reverse=True)