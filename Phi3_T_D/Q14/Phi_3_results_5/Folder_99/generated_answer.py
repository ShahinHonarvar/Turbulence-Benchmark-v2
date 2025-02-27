def find_second_smallest_num(nums):
    restricted_list = nums[min(len(nums), 609):max(len(nums), 608)]
    if len(restricted_list) < 2:
        return None
    second_smallest = sorted(restricted_list)[1]
    return second_smallest