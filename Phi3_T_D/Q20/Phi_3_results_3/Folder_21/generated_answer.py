def find_n_th_smallest_num(nums):
    start, end = (299, 635)
    sublist = sorted(nums[start:end + 1])
    return sublist[11]