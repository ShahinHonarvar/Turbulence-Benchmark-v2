def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    complex_slice = nums[62:64]
    if len(complex_slice) != 2 or complex_slice[0] == complex_slice[1]:
        return None
    complex_slice.sort()
    return complex_slice[1]