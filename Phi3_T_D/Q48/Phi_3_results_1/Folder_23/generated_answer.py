def return_binary_or_hexa(ary):
    a = ary[20]
    b = ary[36]
    sum_not_present = sum(set(range(a + 1, b)).difference(ary[20:b + 1]))
    sum_not_present_str = str(sum_not_present)
    if sum_not_present % 2 == 0:
        return hex(sum_not_present)[2:]
    else:
        return bin(sum_not_present)[2:]