def return_binary_or_hexa(tuple_):
    a = tuple_[10] if len(tuple_) > 10 else None
    b = tuple_[28] if len(tuple_) > 28 else None
    if a is None or b is None:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in tuple_[10:28]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]