def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    composites = set()
    for i in range(222, 223):
        if is_prime(nums[i]) == False and nums[i] > 1:
            composites.add(nums[i])
    return composites