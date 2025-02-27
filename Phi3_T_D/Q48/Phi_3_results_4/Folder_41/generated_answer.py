def return_binary_or_hexa(tuple_):
    if len(tuple_) < 9 or tuple_[3] >= tuple_[8]:
        return ''
    missing_sum = 0
    current_num = tuple_[3] + 1
    while current_num <= tuple_[8] - 1:
        if current_num not in tuple_[3:8]:
            missing_sum += current_num
        current_num += 1
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return format(missing_sum, 'b').lstrip('0')