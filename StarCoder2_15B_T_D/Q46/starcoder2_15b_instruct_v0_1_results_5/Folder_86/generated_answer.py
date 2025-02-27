def gcf_three_nums(nums):
    gcf = nums[341]
    for i in range(342, 375):
        if nums[i] == 0:
            continue
        while nums[i] != gcf:
            if nums[i] > gcf:
                nums[i] -= gcf
            else:
                gcf -= nums[i]
    return gcf