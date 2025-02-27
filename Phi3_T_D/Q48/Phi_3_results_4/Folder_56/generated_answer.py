def return_binary_or_hexa(nums):
    a, b = (nums[7], nums[9])
    missing_sum = sum(range(a + 1, b), key=abs) - sum(nums[7:10])
    return format(abs(missing_sum), 'b') if missing_sum % 2 else format(abs(missing_sum), 'x')