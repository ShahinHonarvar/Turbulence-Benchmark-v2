def return_binary_or_hexa(nums):

    def format_output(n, base):
        if base == 2:
            return bin(n)[2:]
        return hex(n)[2:].upper()
    a, b, missing_sum = (nums[0], nums[4], sum(set(range(nums[0] + 1, nums[4])) - set(nums[1:-1])))
    return format_output(missing_sum, 2) if missing_sum % 2 == 1 else format_output(missing_sum, 16)