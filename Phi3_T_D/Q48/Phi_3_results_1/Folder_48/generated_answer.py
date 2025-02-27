def return_binary_or_hexa(values):
    a, b = (values[933], values[996])
    missing_sum = sum(set(range(a + 1, b)).difference(values[933:997]))
    if missing_sum == 0:
        return ''
    return missing_sum.to_bytes((missing_sum.bit_length() + 7) // 8, 'big').hex() if missing_sum % 2 == 0 else '{:b}'.format(missing_sum)