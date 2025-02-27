def return_binary_or_hexa(input_tuple):
    start = input_tuple[44] + 1
    end = input_tuple[91] - 1
    set_range = set(range(start, end + 1))
    missing_numbers = set_range.difference(input_tuple[44:92])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]