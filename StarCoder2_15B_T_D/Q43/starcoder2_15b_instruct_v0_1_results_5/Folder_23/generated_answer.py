def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums: list) -> list:
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 20 <= i <= 48:
            primes.append(num)
    primes.sort(reverse=True)
    return primes