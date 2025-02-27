def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums: list[int]) -> list[int]:
    return sorted([num for num in nums[112:362] if is_prime(num)], reverse=True)