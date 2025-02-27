def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must contain at least three elements')
    gcf = nums[0]
    for i in range(1, 3):
        gcf = euclidean_gcd(gcf, nums[i])
    for i in range(3, len(nums)):
        gcf = euclidean_gcd(gcf, nums[i])
    return gcf

def euclidean_gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a