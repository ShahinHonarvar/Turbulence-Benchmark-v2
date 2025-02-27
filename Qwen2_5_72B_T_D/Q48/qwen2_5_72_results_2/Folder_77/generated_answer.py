def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    present = set(nums[19:52])
    total_sum = 0
    for i in range(a + 1, b):
        if i not in present:
            total_sum += i
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_solution():
    example_tuple = tuple(range(100))
    print(return_binary_or_hexa(example_tuple))
    modified_tuple = example_tuple[:19] + (99,) + example_tuple[19:52] + (101,) + example_tuple[52:]
    print(return_binary_or_hexa(modified_tuple))