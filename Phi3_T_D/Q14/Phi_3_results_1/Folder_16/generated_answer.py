def find_second_smallest_num(nums):
    relevant_subset = nums[66:78]
    if len(relevant_subset) < 2:
        return None
    second_smallest = float('inf')
    min_element = float('inf')
    for num in relevant_subset:
        if num < min_element:
            second_smallest = min_element
            min_element = num
        elif min_element < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None