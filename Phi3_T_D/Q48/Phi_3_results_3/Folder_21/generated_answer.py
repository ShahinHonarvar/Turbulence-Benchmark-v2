def return_binary_or_hexa(nums):
    end_indices = set(range(15, 58))
    sum_absent = sum((num for i, num in enumerate(nums) if i not in end_indices and a + 1 <= num <= b - 1))
    return f'{sum_absent:b}' if sum_absent % 2 else f'{sum_absent:X}' if sum_absent else ''