def return_binary_or_hexa(integers):
    start, end = (integers[86], integers[99])
    missing_sum = sum((i for i in range(start + 1, end) if i not in integers[86:99 + 1]))
    if missing_sum > 0:
        if missing_sum % 2:
            return bin(missing_sum)[2:]
        else:
            return format(missing_sum, 'x')
    else:
        return ''