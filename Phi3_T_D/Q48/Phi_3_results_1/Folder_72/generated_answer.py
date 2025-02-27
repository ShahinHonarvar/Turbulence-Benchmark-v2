from functools import reduce

def return_binary_or_hexa(num_tuple):
    a = num_tuple[13] + 1
    b = num_tuple[70] - 1
    missing_sum = sum(set(range(a, b + 1)).difference(num_tuple[13:71]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return reduce(lambda x, y: x + y, [hex(digit)[2:] for digit in (missing_sum // 16, missing_sum % 16)], '')