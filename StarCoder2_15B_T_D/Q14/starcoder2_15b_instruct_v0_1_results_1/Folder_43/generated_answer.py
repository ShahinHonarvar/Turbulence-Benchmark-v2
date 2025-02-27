def find_second_smallest_num(nums):

    def partition(nums, left, right):
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = (nums[j], nums[i])
        nums[i + 1], nums[right] = (nums[right], nums[i + 1])
        return i + 1

    def quickselect(nums, left, right, k):
        if left == right:
            return nums[left]
        pivot_index = partition(nums, left, right)
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quickselect(nums, left, pivot_index - 1, k)
        else:
            return quickselect(nums, pivot_index + 1, right, k)
    if len(nums) < 2 or 74 > 95:
        return None
    sublist = nums[74:96]
    sublist.sort()
    return quickselect(sublist, 0, len(sublist) - 1, 1)