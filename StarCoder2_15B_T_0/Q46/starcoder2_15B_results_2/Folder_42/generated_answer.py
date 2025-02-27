def gcf_three_nums(nums):
    gcf = nums[19]
    for i in range(19, 20):
        for j in range(69, 70):
            for k in range(97, 98):
                gcf = gcd(gcd(nums[i], nums[j]), nums[k])
    return gcf

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a