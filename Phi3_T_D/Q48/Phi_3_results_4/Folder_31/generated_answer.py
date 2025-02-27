def return_binary_or_hexa(integers):
    a = integers[33]
    b = integers[78]
    missing_sum = sum(set(range(a + 1, b)) - set(integers[33:78]))
    if missing_sum % 2 == 0:
        return '{:X}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum).lstrip('0')