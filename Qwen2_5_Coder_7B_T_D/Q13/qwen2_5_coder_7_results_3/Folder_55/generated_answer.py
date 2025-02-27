def find_second_largest_num(nums):
    if len(nums) <= 10:
        largest = second_largest = float('-inf')
        for num in nums:
            if num > largest:
                second_largest, largest = (largest, num)
            elif largest > num > second_largest:
                second_largest = num
        return second_largest if second_largest != float('-inf') else None
    else:
        return None