def find_n_th_smallest_num(nums):
    return heapq.nsmallest(7, nums[2:9])[6]