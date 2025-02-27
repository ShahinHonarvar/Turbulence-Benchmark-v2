def return_binary_or_hexa(t):
    start, end = (t[3], t[9])
    present_nums = set(t[3:10])
    missing_nums = [i for i in range(start + 1, end) if i not in present_nums]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]