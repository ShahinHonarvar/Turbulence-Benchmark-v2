def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    return False

def find_primes_between_indices(nums):
    return sorted([n for n in nums[70:72] if is_prime(n)], reverse=True)