def find_second_smallest_num(nums):
    min_num = second_min_num = float('inf')
    count = 0
    for num in nums[:10]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif min_num < num < second_min_num:
            second_min_num = num
        count += 1
        if count > 10:
            break
    return second_min_num if second_min_num != float('inf') else None