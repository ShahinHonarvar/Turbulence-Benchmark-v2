def find_second_largest_num(nums):
    if len(nums) <= 5:
        return None
    top1, top2 = (float('-inf'), float('-inf'))
    for num in nums[:6]:
        if num > top1:
            top2, top1 = (top1, num)
        elif top1 > num > top2:
            top2 = num
    return top2 if top2 != float('-inf') else None