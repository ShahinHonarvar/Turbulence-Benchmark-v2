def return_binary_or_hexa(data):
    try:
        a = data[6] + 1
        b = data[7]
        missing_sum = sum((x for x in range(a, b) if x not in data[6:7]))
        if missing_sum % 2 != 0:
            return format(missing_sum, 'b')
        else:
            return format(missing_sum, 'X')
    except IndexError:
        return ''