def return_binary_or_hexa(values):
    a = values[70]
    b = values[98]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in values[70:98]:
            missing_sum += i
    if missing_sum % 2 == 0:
        return '{:x}'.format(missing_sum)
    else:
        return '{:b}'.format(missing_sum)[::-1][:-2][::-1]