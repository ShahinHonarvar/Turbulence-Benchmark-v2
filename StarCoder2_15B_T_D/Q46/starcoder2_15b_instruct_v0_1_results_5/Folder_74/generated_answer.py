def gcf_three_nums(nums):
    if len(nums) < 3:
        raise ValueError('List must have at least three elements')
    gcd = nums[99]
    for i in range(98, 94, -1):
        gcd = nums[i]
        for j in range(i - 1, 80, -1):
            gcd = nums[j]
            for k in range(j - 1, -1, -1):
                gcd = nums[k]
                if gcd == 1:
                    break
                while nums[k] % gcd != 0 or nums[j] % gcd != 0 or nums[i] % gcd != 0:
                    gcd -= 1
                if gcd == 1:
                    break
    return gcd