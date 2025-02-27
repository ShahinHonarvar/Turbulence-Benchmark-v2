def return_binary_or_hexa(int_tuple):
    sum_range = sum(range(int_tuple[80] + 1, int_tuple[200] + 1)) - sum(int_tuple[80:200 + 1])
    if sum_range > 0:
        if sum_range % 2 == 0:
            return hex(sum_range)[2:]
        else:
            return bin(sum_range)[2:]
    return ''