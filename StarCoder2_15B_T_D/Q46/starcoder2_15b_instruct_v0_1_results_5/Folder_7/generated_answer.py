def gcf_three_nums(nums):
    gcf = nums[477]
    for i in range(477, 697):
        if nums[i] < gcf:
            continue
        for j in range(i + 1, 697):
            if nums[j] < gcf:
                continue
            for k in range(j + 1, 697):
                if nums[k] < gcf:
                    continue
                gcf = max(gcf, gcd(nums[i], nums[j], nums[k]))
    return gcf

def gcd(a, b, c):
    while b != 0:
        a, b = (b, a % b)
    while c != 0:
        a, c = (c, a % c)
    return a