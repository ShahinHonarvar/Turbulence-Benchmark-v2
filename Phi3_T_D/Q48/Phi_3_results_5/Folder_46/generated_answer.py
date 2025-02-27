def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[79])
    all_nums = set(range(a + 1, b))
    range_nums = set(numbers[10:79])
    missing_nums = all_nums - range_nums
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]