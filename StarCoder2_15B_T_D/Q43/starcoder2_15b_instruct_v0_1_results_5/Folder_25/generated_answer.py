def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums: list) -> list:
    primes = []
    for num in nums[52:54]:
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes