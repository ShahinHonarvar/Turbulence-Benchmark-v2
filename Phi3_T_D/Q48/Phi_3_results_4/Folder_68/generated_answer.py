def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[9])
    needed_sum = sum(range(a + 1, b))
    present_sum = sum(tup[1:a] + tup[b:])
    missing_sum = needed_sum - present_sum
    if missing_sum != 0:
        if missing_sum % 2 != 0:
            return f'{missing_sum:b}'.lstrip('0')
        else:
            return f'{missing_sum:x}'.lstrip('0')
    return ''