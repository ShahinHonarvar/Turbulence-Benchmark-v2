def return_binary_or_hexa(nums):
    try:
        start_index, end_index = (25, 80)
        if not 0 <= start_index < len(nums) or not 0 <= end_index < len(nums):
            return ''
        a, b = (nums[start_index], nums[end_index])
        if b <= a:
            return ''
        expected_sum = sum(set(range(a + 1, b)))
        actual_sum = sum((num for num in nums[start_index + 1:end_index] if num < b))
        missing_sum = expected_sum - actual_sum
        if missing_sum > 0 and missing_sum % 2:
            return bin(missing_sum)[2:]
        else:
            return hex(missing_sum)[2:]
    except:
        return ''