def return_binary_or_hexa(nums_tuple):
    if len(nums_tuple) < 7 or not all((isinstance(num, int) and num >= 0 for num in nums_tuple)):
        return ''
    a, b = (sorted(nums_tuple[:7])[0], sorted(nums_tuple[:7])[6])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_tuple))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]