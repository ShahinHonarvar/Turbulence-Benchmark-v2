def find_n_th_smallest_num(nums):
    left, right = (15, 31)
    while left <= right:
        mid = (left + right) // 2
        count = sum([1 for i in range(left, mid + 1) if nums[i] < nums[mid]])
        if count < 10:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]