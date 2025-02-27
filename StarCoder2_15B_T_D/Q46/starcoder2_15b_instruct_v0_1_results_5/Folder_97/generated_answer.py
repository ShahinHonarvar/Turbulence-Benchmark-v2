def gcf_three_nums(nums):
    n944 = nums[944]
    n814 = nums[814]
    n865 = nums[865]
    while n944 != n814:
        if n944 > n814:
            n944 -= n814
        else:
            n814 -= n944
    gcf = n944
    while n865 % gcf != 0:
        gcf = n865 % gcf
    return gcf